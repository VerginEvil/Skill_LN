use clap::Parser;
use skill_ln::cli::Cli;
use skill_ln::commands::execute_command;

#[tokio::main]
async fn main() {
    let cli = Cli::parse();

    if let Some(ref mode) = cli.fallback_mode {
        std::env::set_var("LN_FALLBACK_MODE", mode);
    }

    if let Err(e) = execute_command(cli.command).await {
        eprintln!("[ERROR] skill-ln: {}", e);
        std::process::exit(1);
    }
}
