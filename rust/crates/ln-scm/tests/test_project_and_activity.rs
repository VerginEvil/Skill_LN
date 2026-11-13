use std::path::PathBuf;
use std::sync::Arc;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::sync::Mutex;
use tempfile::tempdir;

use ln_eclipse_compat::AdminFile;
use ln_jca::client::HttpClient;
use ln_scm::activity::*;
use ln_scm::project::*;

#[tokio::test]
async fn test_project_and_activity_lifecycle_mock() {
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

            let req_line = req.lines().next().unwrap_or("");
            let is_numeric_conid = req_line
                .split("conid=")
                .nth(1)
                .map(|r| r.split(['&', ' ']).next().unwrap_or(""))
                .map(|c| !c.is_empty() && c.chars().all(|ch| ch.is_ascii_digit()))
                .unwrap_or(false);

            let (status_line, headers, body) = if req_line.contains("method=connect") {
                ("HTTP/1.1 200 OK", "Set-Cookie: JSESSIONID=scm_s0; Path=/\r\nContent-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>0</conid></ConnectResponse>")
            } else if req_line.contains("method=share") {
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", "<ConnectResponse><SessionID>s</SessionID><conid>1</conid></ConnectResponse>")
            } else if req_line.contains("method=bdecall") && !is_numeric_conid {
                ("HTTP/1.1 500 Internal Server Error", "Content-Type: application/xml\r\n", "<error><info>null</info><message>POST request failed</message><reason>0</reason></error>")
            } else if req.contains("bdename=Application") && req.contains("bdemethod=List") {
                let body = "<ApplicationListResponse><DataArea><Application><name>PM</name><description>Project Management</description><release>10.8</release></Application></DataArea></ApplicationListResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=Application") && req.contains("bdemethod=Show") {
                let body = "<ApplicationShowResponse><DataArea><Application><name>PM</name><description>Project Management</description><release>10.8</release><Package>tc</Package><Package>td</Package></Application></DataArea></ApplicationShowResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=SoftwareProject") && req.contains("bdemethod=List") {
                let body = "<SoftwareProjectListResponse><DataArea><SoftwareProject><projectName>PROJ_1</projectName><projectDescription>Demo Project</projectDescription><projectStatus>active</projectStatus><typeOfProject>standard</typeOfProject><Task><taskName>TASK1</taskName><taskDescription>Initial Task</taskDescription><taskStatus>opened</taskStatus><typeOfTask>feature</typeOfTask><assignedTo>nutdo</assignedTo></Task></SoftwareProject></DataArea></SoftwareProjectListResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=SoftwareProject_V2") && req.contains("bdemethod=Show") {
                let body = "<SoftwareProject_V2ShowResponse><DataArea><SoftwareProject_V2><projectName>PROJ_1</projectName><projectDescription>Demo Project</projectDescription><projectVersionID>B61O_a_ext</projectVersionID><developmentEnvironment>DEV_ENV</developmentEnvironment><developmentRepositoryAddress>PROJ_1_dev</developmentRepositoryAddress><runtimeRepositoryAddress>PROJ_1_rt</runtimeRepositoryAddress><integrationWithPMC>false</integrationWithPMC><Package>tc</Package><Task><taskName>TASK1</taskName><labelUUID>uuid-label-12345</labelUUID><taskUUID>uuid-task-99999</taskUUID><taskVersionID>1</taskVersionID><taskDescription>Initial Task</taskDescription><typeOfTask>feature</typeOfTask><assignedTo>nutdo</assignedTo><taskStatus>opened</taskStatus><taskSeverity>medium</taskSeverity><functionalChange>no</functionalChange></Task></SoftwareProject_V2></DataArea></SoftwareProject_V2ShowResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=SoftwareProject_V2") && req.contains("bdemethod=Change") {
                // new-activity (create task)
                assert!(req.contains("CreateSoftwareTaskV2") || req.contains("<Task actionType=\"create\">"));
                assert!(req.contains("<taskName>TASK2</taskName>"));
                let body = "<SoftwareProject_V2ChangeResponse><DataArea><SoftwareProject_V2><Task><taskName>TASK2</taskName><labelUUID>uuid-label-67890</labelUUID><taskVersionID>1</taskVersionID><taskStatus>created</taskStatus></Task></SoftwareProject_V2></DataArea></SoftwareProject_V2ChangeResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=SoftwareProject") && req.contains("bdemethod=Change") {
                // open-activity (change status to opened)
                assert!(req.contains("<taskStatus>opened</taskStatus>"));
                let body = "<SoftwareProjectChangeResponse><DataArea><SoftwareProject><Task><taskVersionID>2</taskVersionID></Task></SoftwareProject></DataArea></SoftwareProjectChangeResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=CMLabel") && req.contains("bdemethod=GetModifiedComponents") {
                assert!(req.contains("<ActivityID>uuid-label-12345</ActivityID>") || req.contains("<activityUUID>uuid-label-12345</activityUUID>"));
                let body = "<CMLabelResponse><DataArea><ModifiedComponent><name>tcibd001</name><type>table</type><package>tc</package></ModifiedComponent></DataArea></CMLabelResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=CleanActivity") {
                assert!(req.contains("<ActivityID>uuid-label-12345</ActivityID>") || req.contains("<activityUUID>uuid-label-12345</activityUUID>"));
                assert!(req.contains("<CleanActivity>") && req.contains("<ProjectClean>no</ProjectClean>"));
                let body = "<FglStudioResponse><DataArea><Success/></DataArea></FglStudioResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=MoveComponent") {
                assert!(req.contains("<TargetActivityID>"));
                assert!(req.contains("<taskName>TASK_TARGET</taskName>"));
                assert!(req.contains("<labelUUID>uuid-target-8888</labelUUID>"));
                assert!(req.contains("<Component><type>table</type><name>tcibd001</name></Component>"));
                let body = "<FglStudioResponse><DataArea><result>ok</result></DataArea></FglStudioResponse>";
                ("HTTP/1.1 200 OK", "Content-Type: application/xml\r\n", body)
            } else if req.contains("bdename=FglStudio") && req.contains("bdemethod=CleanComponents") {
                assert!(req.contains("<CleanComponents>"));
                assert!(req.contains("<Component><type>table</type><name>tcibd001</name></Component>"));
                let body = "<FglStudioResponse><DataArea><result>ok</result></DataArea></FglStudioResponse>";
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

    // 1. list_applications
    let apps = list_applications(&client).await.unwrap();
    assert_eq!(apps.len(), 1);
    assert_eq!(apps[0].name, "PM");
    assert_eq!(apps[0].description, "Project Management");
    assert_eq!(apps[0].release, "10.8");

    // 2. show_application
    let app_det = show_application(&client, "PM").await.unwrap();
    assert_eq!(app_det.name, "PM");
    assert_eq!(app_det.packages, vec!["tc", "td"]);

    // 3. list_software_projects
    let projs = list_software_projects(&client).await.unwrap();
    assert_eq!(projs.len(), 1);
    assert_eq!(projs[0].name, "PROJ_1");
    assert_eq!(projs[0].tasks.len(), 1);
    assert_eq!(projs[0].tasks[0].task_name, "TASK1");

    // 4. get_software_project_details
    let proj_det = get_software_project_details(&client, "PROJ_1", None).await.unwrap();
    assert_eq!(proj_det.project_name, "PROJ_1");
    assert_eq!(proj_det.base_vrc, "B61O_a_ext");
    assert_eq!(proj_det.development_repository_address, "PROJ_1_dev");
    assert_eq!(proj_det.runtime_repository_address, "PROJ_1_rt");
    assert_eq!(proj_det.tasks.len(), 1);
    // Invariant: labelUUID vs taskUUID
    assert_eq!(proj_det.tasks[0].label_uuid, "uuid-label-12345");
    assert_eq!(proj_det.tasks[0].task_uuid, "uuid-task-99999");

    // 5. list_remote_activities & get_remote_activity_details
    let act_list = list_remote_activities(&client, "PROJ_1").await.unwrap();
    assert_eq!(act_list.len(), 1);
    assert_eq!(act_list[0].label_uuid, "uuid-label-12345");

    let act_one = get_remote_activity_details(&client, "PROJ_1", "TASK1").await.unwrap();
    assert!(act_one.is_some());
    assert_eq!(act_one.unwrap().label_uuid, "uuid-label-12345");

    // 6. create_remote_activity
    let tmp = tempdir().unwrap();
    let ws = tmp.path();
    let create_res = create_remote_activity(
        &client,
        "PROJ_1",
        "TASK2",
        CreateActivityOptions {
            description: "New Task 2",
            assigned_to: "nutdo",
            type_of_task: "enhancement",
            ..Default::default()
        },
    ).await.unwrap();
    assert_eq!(create_res.task_id, "TASK2");
    assert_eq!(create_res.label_uuid, "uuid-label-67890");
    assert_eq!(create_res.status, "created");

    // 7. open_remote_activity
    let open_res = open_remote_activity(
        &client,
        "PROJ_1",
        "TASK1",
        Some(ws),
        false,
    ).await.unwrap();
    assert_eq!(open_res.status, "opened");
    assert_eq!(open_res.label_uuid, "uuid-label-12345");
    assert_eq!(open_res.task_version_id, "2");
    assert!(open_res.workspace_path.is_some());

    let act_folder = PathBuf::from(open_res.workspace_path.unwrap());
    assert!(act_folder.join(".project").exists());
    assert!(act_folder.join(".admin").exists());
    assert!(act_folder.join(".settings").join("properties.index").exists());

    // 8. clean_remote_activity
    let clean_ok = clean_remote_activity(&client, "PROJ_1", "TASK1", Some("uuid-label-12345"), false).await.unwrap();
    assert!(clean_ok);

    // 9. move_activity_components & clean_activity_components
    let src_tbl = act_folder.join("tc").join("table").join("ibd").join("tcibd001.tbl");
    std::fs::create_dir_all(src_tbl.parent().unwrap()).unwrap();
    std::fs::write(&src_tbl, "<DR_Table name=\"tcibd001\"/>").unwrap();
    let mut admin_f = AdminFile::new();
    admin_f.after_get("tc/table/ibd/tcibd001.tbl");
    admin_f.save_to_path(&act_folder.join(".admin")).unwrap();

    let target_dir = ws.join("TASK_TARGET [PROJ_1]");
    std::fs::create_dir_all(&target_dir).unwrap();
    AdminFile::new().save_to_path(&target_dir.join(".admin")).unwrap();

    let move_res = move_activity_components(
        &client,
        &[ComponentRef { name: "tcibd001".to_string(), comp_type: "table".to_string() }],
        &act_folder,
        "TASK_TARGET",
        "uuid-target-8888",
        "B61O_a_ext",
        "PROJ_1_dev",
        Some(&target_dir),
    ).await.unwrap();
    assert!(move_res.success);
    assert_eq!(move_res.moved_components, 1);
    assert!(!src_tbl.exists());
    assert!(target_dir.join("tc").join("table").join("ibd").join("tcibd001.tbl").exists());

    // 10. clean_activity_components
    let clean_res = clean_activity_components(
        &client,
        &[ComponentRef { name: "tcibd001".to_string(), comp_type: "table".to_string() }],
        &target_dir,
    ).await.unwrap();
    assert!(clean_res.success);
    assert_eq!(clean_res.cleaned_components, 1);
    assert!(!target_dir.join("tc").join("table").join("ibd").join("tcibd001.tbl").exists());
}
