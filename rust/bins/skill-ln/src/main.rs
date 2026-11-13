use clap::Parser;
use skill_ln::cli::Cli;
use skill_ln::commands::execute_command;

const MAIN_STACK_SIZE: usize = 8 * 1024 * 1024;

fn main() {
    let builder = std::thread::Builder::new()
        .name("skill-ln-main".to_string())
        .stack_size(MAIN_STACK_SIZE);

    let handle = builder
        .spawn(|| {
            let cli = Cli::parse();

            if let Some(ref mode) = cli.fallback_mode {
                std::env::set_var("LN_FALLBACK_MODE", mode);
            }

            let rt = tokio::runtime::Builder::new_multi_thread()
                .enable_all()
                .thread_stack_size(MAIN_STACK_SIZE)
                .build()
                .expect("Failed to create Tokio runtime");

            rt.block_on(async move {
                if let Err(e) = Box::pin(execute_command(cli.command)).await {
                    eprintln!("[ERROR] skill-ln: {}", e);
                    std::process::exit(1);
                }
            });
        })
        .expect("Failed to spawn skill-ln main thread");

    if handle.join().is_err() {
        std::process::exit(1);
    }
}
