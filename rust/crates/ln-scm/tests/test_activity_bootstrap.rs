use ln_eclipse_compat::{AdminFile, PropertyBucket};
use ln_scm::activity::bootstrap_local_activity;
use tempfile::tempdir;

#[test]
fn test_bootstrap_local_activity_creates_all_metadata() {
    let tmp = tempdir().unwrap();
    let ws_path = tmp.path();

    let task_id = "TASK100";
    let project_name = "PM_DEMO";
    let activity_uuid = "00000000-1111-2222-3333-444444444444";
    let dev_conn = "PM_DEMO_dev";

    let act_dir = bootstrap_local_activity(
        ws_path,
        task_id,
        project_name,
        activity_uuid,
        dev_conn,
    ).unwrap();

    let folder_name = format!("{task_id} [{project_name}]");
    assert_eq!(act_dir, ws_path.join(&folder_name));
    assert!(act_dir.exists());

    // 1. Verify .project
    let proj_file = act_dir.join(".project");
    assert!(proj_file.exists());
    let proj_xml = std::fs::read_to_string(&proj_file).unwrap();
    assert!(proj_xml.contains(&format!("<name>{folder_name}</name>")));
    assert!(proj_xml.contains("com.infor.ln.studio.apps.core.bic"));
    assert!(proj_xml.contains("com.infor.ln.studio.apps.core.fourglStudio"));

    // 2. Verify .admin
    let admin_file = act_dir.join(".admin");
    assert!(admin_file.exists());
    let af = AdminFile::load_from_path(&admin_file).unwrap();
    assert_eq!(af.entries.len(), 0);

    // 3. Verify workspace binary properties.index
    let meta_idx = ws_path
        .join(".metadata")
        .join(".plugins")
        .join("org.eclipse.core.resources")
        .join(".projects")
        .join(&folder_name)
        .join(".indexes")
        .join("properties.index");
    assert!(meta_idx.exists());
    let bucket = PropertyBucket::load_from_path(&meta_idx).unwrap();
    assert_eq!(bucket.get_property("ProjectName", "", "").unwrap(), project_name);
    assert_eq!(bucket.get_property("TaskName", "", "").unwrap(), task_id);
    assert_eq!(bucket.get_property("Label", "", "").unwrap(), activity_uuid);
    assert_eq!(bucket.get_property("DevelopmentTimeRepositoryAddress", "", "").unwrap(), dev_conn);
    assert_eq!(bucket.get_property("RunTimeRepositoryAddress", "", "").unwrap(), "PM_DEMO_rt");
    assert_eq!(bucket.get_property("ApplicationUsesSCM", "", "").unwrap(), "yes");
    assert_eq!(bucket.get_property("TaskStatus", "", "").unwrap(), "opened");
    assert_eq!(
        bucket.get_property("repository", "org.eclipse.team.core", "").unwrap(),
        "com.infor.ln.studio.apps.core.cmprovider"
    );

    // 4. Verify text .settings/properties.index
    let settings_file = act_dir.join(".settings").join("properties.index");
    assert!(settings_file.exists());
    let settings_txt = std::fs::read_to_string(&settings_file).unwrap();
    assert!(settings_txt.contains("version=1"));
    assert!(settings_txt.contains(&format!("activityUUID={activity_uuid}")));
    assert!(settings_txt.contains(&format!("softwareProject={project_name}")));
    assert!(settings_txt.contains(&format!("connectionPoint={dev_conn}")));
    assert!(settings_txt.contains(&format!("taskId={task_id}")));
}
