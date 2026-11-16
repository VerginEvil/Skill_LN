use clap::{Parser, Subcommand};

#[derive(Parser, Debug)]
#[command(
    name = "skill-ln",
    author = "Skill_LN Team",
    version = "1.0.0",
    about = "Unified 100% Native Infor LN Studio & Baan 4GL CLI / MCP Server"
)]
pub struct Cli {
    /// Global fallback mode: auto | strict | off (can also be set via LN_FALLBACK_MODE)
    #[arg(long, global = true)]
    pub fallback_mode: Option<String>,

    #[command(subcommand)]
    pub command: Commands,
}

#[derive(Subcommand, Debug)]
pub enum Commands {
    // === 1.1 Environment & Auth ===
    #[command(about = "List customer workspaces and activity folders")]
    Workspace {
        #[arg(long)]
        list: bool,
        #[arg(long)]
        activities: bool,
    },

    #[command(about = "List configured cloud environments and connection endpoints")]
    Environments {
        #[arg(long)]
        workspace_root: Option<String>,
    },

    #[command(about = "Multi-channel OAuth2 SSO login and status check")]
    Login {
        #[arg(long)]
        workspace: Option<String>,
        #[arg(long)]
        ionapi: Option<String>,
        #[arg(long)]
        status: bool,
        #[arg(long)]
        check_only: bool,
        #[arg(long)]
        json: bool,
        #[arg(long)]
        register_protocol: bool,
    },

    #[command(about = "Import .ionapi credentials and synchronize Eclipse preferences")]
    Connect {
        #[arg(long)]
        ionapi: String,
        #[arg(long)]
        workspace: Option<String>,
        #[arg(long)]
        manual_auth: bool,
    },

    #[command(about = "Manage persistent background Single-Leader daemon")]
    Daemon {
        #[arg(long)]
        status: bool,
        #[arg(long)]
        stop: bool,
        #[arg(long)]
        restart: bool,
        #[arg(long)]
        token: Option<String>,
    },

    // === 1.2 Project & Activity ===
    #[command(about = "Browse remote applications and software projects")]
    Project {
        #[arg(long)]
        app: Option<String>,
        #[arg(long)]
        project: Option<String>,
    },

    #[command(name = "project-info", about = "Inspect software project metadata and VRC configuration")]
    ProjectInfo {
        #[arg(long)]
        project: String,
    },

    #[command(about = "Browse activities under a software project")]
    Activity {
        #[arg(long)]
        project: String,
        #[arg(long)]
        activity: Option<String>,
    },

    #[command(name = "new-activity", about = "Create new activity on LN server and bootstrap local workspace")]
    NewActivity {
        #[arg(long)]
        project: String,
        #[arg(long)]
        task: String,
        #[arg(long)]
        desc: Option<String>,
        #[arg(long)]
        user: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
    },

    #[command(name = "open-activity", about = "Open and bootstrap an existing activity locally")]
    OpenActivity {
        #[arg(long)]
        project: String,
        #[arg(long)]
        task: String,
        #[arg(long)]
        no_sync_modified: bool,
        #[arg(long)]
        workspace: Option<String>,
    },

    #[command(name = "clean-activity", about = "Clean stuck workarea lock on LN server")]
    CleanActivity {
        #[arg(long)]
        project: String,
        #[arg(long)]
        task: String,
    },

    #[command(name = "move-components", about = "Move components between development activities")]
    MoveComponents {
        #[arg(long)]
        source_activity: String,
        #[arg(long)]
        target_task: String,
        #[arg(long)]
        components: String,
    },

    #[command(name = "clean-components", about = "Release locks and remove components from activity")]
    CleanComponents {
        #[arg(long)]
        activity: String,
        #[arg(long)]
        components: String,
    },

    // === 1.3 Explorer, Remote Fetch & SCM ===
    #[command(about = "Browse components across all 12 types with wildcard filters")]
    Explorer {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        filter: Option<String>,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
    },

    #[command(name = "get-component", about = "Fetch component from server (inspect, read-only download, or script export)")]
    GetComponent {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        inspect: bool,
        #[arg(long)]
        export_script: Option<String>,
        #[arg(long)]
        activity: Option<String>,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
    },

    #[command(name = "sync-reference", about = "Sync read-only reference components into .reference/ and update DD cache")]
    SyncReference {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        workspace_dir: Option<String>,
        #[arg(long)]
        dd_cache: Option<String>,
    },

    #[command(name = "clone-component", about = "Clone standard or custom component into renamed custom activity component")]
    CloneComponent {
        #[arg(long)]
        source_type: String,
        #[arg(long)]
        source_name: String,
        #[arg(long)]
        target_name: String,
        #[arg(long)]
        activity: String,
        #[arg(long)]
        target_desc: Option<String>,
    },

    #[command(name = "checkout-component", about = "Check out component on server and download editable Single-XML")]
    CheckoutComponent {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        activity: String,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
        #[arg(long)]
        comment: Option<String>,
    },

    #[command(name = "uncheckout-component", about = "Revert component check-out on server and restore read-only copy")]
    UncheckoutComponent {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        activity: String,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
    },

    #[command(name = "checkin-component", about = "Put component to server and check in for LN UI Cloud testing")]
    CheckinComponent {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        activity: String,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
        #[arg(long)]
        comment: Option<String>,
    },

    #[command(name = "checkout-activity", about = "Batch check-out all components in an activity ordered by architectural dependency")]
    CheckoutActivity {
        #[arg(long)]
        activity: String,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
    },

    #[command(name = "checkin-activity", about = "Batch check-in all modified components in an activity with a single comment")]
    CheckinActivity {
        #[arg(long)]
        activity: String,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
        #[arg(long)]
        comment: Option<String>,
    },

    #[command(name = "end-activity", about = "Hard-blocked pre-commit delivery gate (raises PreCommitBoundaryError)")]
    EndActivity {
        #[arg(long)]
        task: String,
        #[arg(long)]
        project: String,
    },

    #[command(name = "prepare-end-activity", about = "Pre-commit verification gate before human handoff")]
    PrepareEndActivity {
        #[arg(long)]
        activity: String,
        #[arg(long)]
        project: Option<String>,
        #[arg(long)]
        workspace: Option<String>,
    },

    // === 1.4 Code Intelligence, Revision History & Diff ===
    #[command(name = "compile-source", about = "Ad-hoc server compilation via FglStudio without committing")]
    CompileSource {
        #[arg(long)]
        package: String,
        #[arg(long)]
        source_file: Option<String>,
        #[arg(long)]
        code: Option<String>,
        #[arg(long)]
        flags: Option<String>,
    },

    #[command(name = "search-server", about = "Global server regex search across packages via FglStudio")]
    SearchServer {
        #[arg(long)]
        pattern: String,
        #[arg(long)]
        package: Option<String>,
    },

    #[command(name = "call-hierarchy", about = "Call hierarchy and where-used analysis")]
    CallHierarchy {
        #[arg(long)]
        source_file: String,
        #[arg(long)]
        function: String,
        #[arg(long, default_value = "callers")]
        mode: String,
    },

    #[command(name = "open-declaration", about = "Jump to symbol declaration on server")]
    OpenDeclaration {
        #[arg(long)]
        comp: String,
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        function: String,
    },

    #[command(name = "related-components", about = "Discover script-referenced components")]
    RelatedComponents {
        #[arg(long)]
        package: String,
        #[arg(long)]
        source_file: Option<String>,
        #[arg(long)]
        code: Option<String>,
    },

    #[command(about = "Query server revision history and commit logs")]
    Revisions {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        version: Option<String>,
    },

    #[command(name = "diff-component", about = "Script and structural XML diff against server revisions")]
    DiffComponent {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        activity: String,
        #[arg(long)]
        revision: Option<i32>,
    },

    #[command(name = "generate-report-server", about = "Generate report structure on server via DR_Report wizard")]
    GenerateReportServer {
        #[arg(long)]
        code: String,
        #[arg(long)]
        table: String,
        #[arg(long, default_value = "132")]
        paper_width: String,
        #[arg(long, default_value = "1")]
        report_type: String,
        #[arg(long)]
        activity: Option<String>,
    },

    // === 1.5 Component Generation & Pipeline ===
    #[command(about = "Generate Table, Label & Domain XML from schema")]
    Table {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Generate Domain XML independently")]
    Domain {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Generate Session XML")]
    Session {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Generate Library XML (Standard DLL)")]
    Library {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Generate Menu XML and Labels")]
    Menu {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Generate Message (.msg) XML")]
    Message {
        #[arg(long)]
        code: String,
        #[arg(long, default_value = "1")]
        severity: String,
        #[arg(long)]
        text: Option<String>,
        #[arg(long)]
        activity: String,
    },

    #[command(about = "Generate Question (.qst) XML")]
    Question {
        #[arg(long)]
        code: String,
        #[arg(long)]
        domain: Option<String>,
        #[arg(long)]
        text: Option<String>,
        #[arg(long)]
        activity: String,
    },

    #[command(about = "Generate Include Function (.fnc) XML")]
    Function {
        #[arg(long)]
        code: String,
        #[arg(long)]
        script_file: Option<String>,
        #[arg(long)]
        activity: String,
    },

    #[command(about = "Generate Additional File (.add) XML")]
    Additional {
        #[arg(long)]
        code: String,
        #[arg(long)]
        content_file: Option<String>,
        #[arg(long)]
        activity: String,
    },

    #[command(about = "Generate Report (.rpt) XML")]
    Report {
        #[arg(long)]
        code: String,
        #[arg(long, default_value = "132")]
        paper_width: String,
        #[arg(long)]
        activity: String,
    },

    #[command(about = "Generate all components declared in schema in one pass")]
    Component {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Full autonomous pipeline (Gen -> Sync -> Validate -> Build)")]
    Pipeline {
        #[arg(long)]
        spec: String,
        #[arg(long)]
        output_dir: Option<String>,
        #[arg(long)]
        auto_fix: bool,
        #[arg(long)]
        skip_build: bool,
    },

    // === 1.6 Extension Modeler Helpers ===
    #[command(name = "new-extension", about = "Scaffold local extension .4gl script with #context_on blocks")]
    NewExtension {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        target: String,
        #[arg(long)]
        output: Option<String>,
    },

    #[command(name = "import-extension", about = "Import extension script from Studio Get cache into local file")]
    ImportExtension {
        #[arg(long)]
        source: String,
        #[arg(long)]
        output: Option<String>,
    },

    #[command(name = "extension-hooks", about = "Inspect and extract clean hook blocks for pasting into LN UI")]
    ExtensionHooks {
        script_path: String,
        #[arg(long)]
        list: bool,
        #[arg(long)]
        hook: Option<String>,
        #[arg(long)]
        copy: bool,
    },

    // === 1.7 Validation, Diagnostics, Build & SCM ===
    #[command(name = "check-script", about = "Offline static 4GL syntax, block balance, and hook check")]
    CheckScript {
        file_path: String,
        #[arg(long)]
        strict: bool,
        #[arg(long)]
        json: bool,
    },

    #[command(about = "4-layer activity validation (.admin, XML, cross-ref, 4GL)")]
    Validate {
        activity_path: Option<String>,
        #[arg(long)]
        strict: bool,
        #[arg(long)]
        fix: bool,
        #[arg(long)]
        json: bool,
    },

    #[command(name = "sync-admin", about = "Synchronize 12-extension SCM .admin registration cache")]
    SyncAdmin {
        #[arg(long)]
        activity: String,
    },

    #[command(about = "Decode Eclipse binary problem markers (.markers)")]
    Diagnose {
        #[arg(long)]
        activity: String,
        #[arg(long)]
        errors_only: bool,
    },

    #[command(about = "Trigger JCA remote compile or workbench UI build")]
    Build {
        #[arg(long)]
        activity: String,
        #[arg(long)]
        ui_bridge: bool,
    },

    #[command(name = "deploy-test", about = "Push local component changes to server Activity VRC for testing")]
    DeployTest {
        #[arg(long = "type")]
        comp_type: String,
        #[arg(long)]
        name: String,
        #[arg(long)]
        activity: String,
        #[arg(long, default_value = "compile-only")]
        mode: String,
        #[arg(long)]
        dry_run: bool,
    },

    #[command(about = "Inject 4GL script into Single-XML <expression>")]
    Inject {
        #[arg(long)]
        source: String,
        #[arg(long)]
        target: String,
    },

    #[command(about = "Extract 4GL script from Single-XML <expression>")]
    Extract {
        #[arg(long)]
        source: String,
        #[arg(long)]
        output: String,
    },

    #[command(name = "mcp-setup", about = "Register Stdio MCP Server in client configuration")]
    McpSetup {
        #[arg(long, default_value = "generic")]
        client: String,
        #[arg(long)]
        apply: bool,
    },

    #[command(name = "mcp-stdio", about = "Start native JSON-RPC 2.0 MCP server over stdio")]
    McpStdio,

    // === Unified Native Rust Commands ===
    #[command(name = "audit-4gl", about = "Audit 4GL file or directory with 25 rules")]
    Audit4gl {
        path: String,
        #[arg(long)]
        rule: Option<String>,
        #[arg(long)]
        json: bool,
        #[arg(long)]
        dd_cache: Option<String>,
    },

    #[command(name = "fn-search", about = "Instant zero-copy search across 2,266 bshell functions")]
    FnSearch {
        query: String,
        #[arg(long)]
        category: Option<String>,
        #[arg(long, default_value = "20")]
        limit: usize,
        #[arg(long)]
        json: bool,
    },

    #[command(name = "doc-search", about = "Search Infor LN Studio programmer guides and references")]
    DocSearch {
        query: String,
        #[arg(long, default_value = "10")]
        limit: usize,
        #[arg(long)]
        json: bool,
    },

    #[command(name = "verify-studio-build", about = "Zero-dependency JVM .class and owtemplates build differ")]
    VerifyStudioBuild {
        #[arg(long)]
        studio_home: String,
        #[arg(long)]
        json: bool,
    },
}
