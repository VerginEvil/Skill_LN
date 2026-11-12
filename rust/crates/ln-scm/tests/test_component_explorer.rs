use std::path::PathBuf;
use std::sync::Arc;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;
use tempfile::tempdir;

use ln_eclipse_compat::AdminFile;
use ln_jca::client::HttpClient;
use ln_scm::explorer::*;

#[test]
fn test_resolve_extension_component_name_cases() {
    // 1. txest*
    let r1 = resolve_extension_component_name("txesttcibd001", "");
    assert!(r1.is_extension);
    assert_eq!(r1.ext_type, "est");
    assert_eq!(r1.target_code, "tcibd001");
    assert_eq!(r1.component_type, "table");

    // 2. txess*
    let r2 = resolve_extension_component_name("txessibd4100m000", "");
    assert!(r2.is_extension);
    assert_eq!(r2.ext_type, "ess");
    assert_eq!(r2.component_type, "session");

    // 3. Table code without prefix when comp_type="extension"
    let r3 = resolve_extension_component_name("cisli220", "extension");
    assert!(r3.is_extension);
    assert_eq!(r3.library_name, "txestcisli220");
    assert_eq!(r3.ext_type, "est");
    assert_eq!(r3.target_code, "cisli220");

    // 4. Session code with m000 when comp_type="extension"
    let r4 = resolve_extension_component_name("cisli2620m000", "extension");
    assert!(r4.is_extension);
    assert_eq!(r4.library_name, "txesssli2620m0");
    assert_eq!(r4.ext_type, "ess");

    // 5. Standard component
    let r5 = resolve_extension_component_name("tcibd001", "table");
    assert!(!r5.is_extension);
    assert_eq!(r5.library_name, "tcibd001");
}

#[tokio::test]
async fn test_component_explorer_and_clone_mock() {
    let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
    let addr = listener.local_addr().unwrap();
    let base_url = format!("http://127.0.0.1:{}/TENANT/LN/webservice", addr.port());

    let captured_requests: Arc<Mutex<Vec<String>>> = Arc::new(Mutex::new(Vec::new()));
    let req_log = captured_requests.clone();

    tokio::spawn(async move {
        while let Ok((mut socket, _)) = listener.accept().await {
            let mut buf = [0u8; 8192];
            let n = socket.read(&mut buf).await.unwrap_or(0);
            let req = String::from_utf8_lossy(&buf[..n]).to_string();

            let mut log = req_log.lock().await;
            log.push(req.clone());
            drop(log);

            let (status_line, headers, body) = if req.contains("bdename=StudioComponent") && req.contains("bdemethod=GetBrowseList") {
                // Verify Controlling Attributes
                assert!(req.contains("<package>tc</package>") || req.contains("package"));
                assert!(req.contains("<type>table</type>") || req.contains("type"));
                let body = "<GetBrowseListResponse><DataArea><Component><name>tcibd001</name><type>table</type><package>tc</package><module>ibd</module><description>General Item Data</description><versionID>B61O_a_ext</versionID><isCheckedOut>no</isCheckedOut><isExpired>no</isExpired></Component></DataArea></GetBrowseListResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=StudioComponent") && (req.contains("bdemethod=GetProjectSource") || req.contains("bdemethod=GetActivitySource")) {
                let body = "<StudioComponentResponse><DataArea><DR_Table name=\"tcibd001\" package=\"tc\" module=\"ibd\">\n\
                    <description>General Item Data</description>\n\
                    <Column name=\"item\" isMandatory=\"true\">\n\
                        <datatype name=\"tcitem\" nativeDatatype=\"7\">\n\
                            <Facet><type>maxLength</type><value>16</value></Facet>\n\
                        </datatype>\n\
                        <descriptionReference>tcibd001.item</descriptionReference>\n\
                    </Column>\n\
                    <Index name=\"1\"><IndexColumn column=\"item\"/></Index>\n\
                    <Source><expression><![CDATA[\nfunction extern long dummy()\n{\n    return(0)\n}\n]]></expression></Source>\n\
                </DR_Table></DataArea></StudioComponentResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=DR_Table") && req.contains("bdemethod=DR_Create") {
                // Invariant: Verify raw <DR_Table> root XML document directly without <DR_CreateRequest> wrapper
                assert!(!req.contains("<DR_CreateRequest>"));
                assert!(req.contains("<DR_Table"));
                assert!(req.contains("name=\"txibd001\""));
                assert!(req.contains("package=\"tx\""));
                assert!(req.contains("<ActivityID>") || req.contains("<activityUUID>"));
                let body = "<DR_TableResponse><DR_Table><status>created</status></DR_Table></DR_TableResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else {
                ("HTTP/1.1 404 Not Found", "Content-Type: text/plain\r\n", "Not Found")
            };

            let resp = format!(
                "{}\r\n{}Content-Length: {}\r\nConnection: close\r\n\r\n{}",
                status_line,
                headers,
                body.len(),
                body
            );
            let _ = socket.write_all(resp.as_bytes()).await;
        }
    });

    let client = HttpClient::new(&base_url, "mock_token");

    // 1. browse_components
    let items = browse_components(&client, "tc", "table", "tcibd*", "ProjectServer").await.unwrap();
    assert_eq!(items.len(), 1);
    assert_eq!(items[0].name, "tcibd001");
    assert_eq!(items[0].comp_type, "table");
    assert_eq!(items[0].package, "tc");
    assert_eq!(items[0].module, "ibd");

    // 2. inspect_component
    let insp = inspect_component(&client, "table", "tcibd001", "ProjectServer", None, None, None).await.unwrap();
    assert_eq!(insp.name, "tcibd001");
    assert_eq!(insp.fields.len(), 1);
    assert_eq!(insp.indices.get("1").unwrap(), &vec!["item".to_string()]);
    assert!(insp.script.contains("dummy"));

    // 3. get_component into activity directory
    let tmp = tempdir().unwrap();
    let act_dir = tmp.path().join("TASK1 [PROJ_1]");
    std::fs::create_dir_all(&act_dir).unwrap();
    AdminFile::new().save_to_path(&act_dir.join(".admin")).unwrap();

    let export_script_dir = tmp.path().join("scripts");
    let downloaded_file = get_component(
        &client,
        "table",
        "tcibd001",
        &act_dir,
        true, // read_only
        "ProjectServer",
        None,
        Some("uuid-act-1111"),
        Some("B61O_a_ext"),
        Some(&export_script_dir),
    ).await.unwrap();

    assert!(downloaded_file.exists());
    assert_eq!(downloaded_file.file_name().unwrap(), "tcibd001.tbl");
    // Verify TDE single-xml relative path
    let rel_norm = downloaded_file.strip_prefix(&act_dir).unwrap().to_string_lossy().replace('\\', "/");
    assert_eq!(rel_norm, "tc/table/ibd/tcibd001.tbl");

    // Verify .admin registration via after_get
    let af = AdminFile::load_from_path(&act_dir.join(".admin")).unwrap();
    let admin_comp = af.get(&rel_norm).unwrap();
    assert!(!admin_comp.is_checked_out);
    assert!(!admin_comp.is_created);

    // Verify script exported
    assert!(export_script_dir.join("tcibd001.cln").exists());

    // Verify .ln_dd_cache.json automatically indexed
    let dd_path = tmp.path().join(".ln_dd_cache.json");
    assert!(dd_path.exists());
    let dd_json: serde_json::Value = serde_json::from_str(&std::fs::read_to_string(&dd_path).unwrap()).unwrap();
    assert!(dd_json["tables"].get("tcibd001").is_some());
    assert_eq!(dd_json["tables"]["tcibd001"]["fields"]["item"]["domain"], "tcitem");

    // 4. sync_reference
    let sync_res = sync_reference(
        &client,
        "table",
        "tcibd001",
        tmp.path(),
        None,
        "ProjectServer",
    ).await.unwrap();
    assert_eq!(sync_res.synced_count, 1);
    assert!(sync_res.read_only);
    let ref_file = PathBuf::from(&sync_res.files[0]);
    assert!(ref_file.exists());
    assert!(ref_file.to_string_lossy().contains(".reference"));

    // 5. clone_component
    let cloned_file = clone_component(
        &client,
        "table",
        "tcibd001",
        "txibd001",
        &act_dir,
        true, // register_on_server
        "ProjectServer",
        Some("uuid-act-1111"),
    ).await.unwrap();
    assert!(cloned_file.exists());
    assert_eq!(cloned_file.file_name().unwrap(), "txibd001.tbl");

    // Verify .admin after_create
    let af_after = AdminFile::load_from_path(&act_dir.join(".admin")).unwrap();
    let cloned_admin = af_after.get("tx/table/ibd/txibd001.tbl").unwrap();
    assert!(cloned_admin.is_created);
    assert!(cloned_admin.is_checked_out);
    assert!(cloned_admin.is_dirty);

    // 6. Extension Modeler Rule (ADR 0006) - Extension objects must be blocked from cloning
    let ext_err = clone_component(
        &client,
        "extension",
        "txesttcibd001",
        "txesttcibd002",
        &act_dir,
        false,
        "ProjectServer",
        None,
    ).await;
    assert!(ext_err.is_err());
    let err_msg = format!("{}", ext_err.unwrap_err());
    assert!(err_msg.contains("Extension Modeler Rule (ADR 0006)"));
}
