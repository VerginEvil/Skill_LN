use clap::Parser;
use skill_ln::cli::Cli;
use skill_ln::commands::execute_command;

#[tokio::test]
async fn test_cli_fn_search_and_doc_search() {
    let fn_cli = Cli::parse_from(["skill-ln", "fn-search", "dal.set.error", "--limit", "5", "--json"]);
    let res = execute_command(fn_cli.command).await;
    assert!(res.is_ok(), "fn-search must succeed");

    let doc_cli = Cli::parse_from(["skill-ln", "doc-search", "dal2", "--limit", "3", "--json"]);
    let res_doc = execute_command(doc_cli.command).await;
    assert!(res_doc.is_ok(), "doc-search must succeed");
}

#[tokio::test]
async fn test_cli_end_activity_gate_hard_blocked() {
    let end_cli = Cli::parse_from([
        "skill-ln", "end-activity",
        "--task", "task_01",
        "--project", "EXTce01107",
    ]);

    let err = execute_command(end_cli.command).await;
    assert!(err.is_err(), "end-activity must be hard-blocked");
    let err_msg = err.unwrap_err().to_string();
    assert!(
        err_msg.contains("PreCommitBoundaryError"),
        "Error message must contain PreCommitBoundaryError, got: {}",
        err_msg
    );
}

#[tokio::test]
async fn test_cli_checkout_component_extension_blocked() {
    let chk_cli = Cli::parse_from([
        "skill-ln", "checkout-component",
        "--type", "library",
        "--name", "txesssli2620m0",
        "--activity", "test_act",
    ]);

    let err = execute_command(chk_cli.command).await;
    assert!(err.is_err(), "checkout on tx* extension component must fail");
    let err_msg = err.unwrap_err().to_string();
    assert!(
        err_msg.contains("ReadOnlyComponentError"),
        "Error message must contain ReadOnlyComponentError, got: {}",
        err_msg
    );
}

#[tokio::test]
async fn test_cli_mcp_setup_output() {
    let setup_cli = Cli::parse_from(["skill-ln", "mcp-setup", "--client", "generic"]);
    let res = execute_command(setup_cli.command).await;
    assert!(res.is_ok());
}
