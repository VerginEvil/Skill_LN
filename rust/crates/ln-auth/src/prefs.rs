use std::collections::{BTreeMap, HashMap};
use std::fs::File;
use std::io::{self, Read, Write};
use std::path::Path;
use crate::ionapi::IonapiConfig;

/// Reads an Eclipse .prefs file into a key-value map, unescaping `\:` and `\=`.
pub fn read_prefs_file(path: &Path) -> io::Result<BTreeMap<String, String>> {
    let mut map = BTreeMap::new();
    if !path.exists() {
        return Ok(map);
    }

    let mut file = File::open(path)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    for line in content.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty() || trimmed.starts_with('#') {
            continue;
        }
        if let Some(eq_idx) = trimmed.find('=') {
            let k = trimmed[..eq_idx].trim().replace(r"\:", ":").replace(r"\=", "=");
            let v = trimmed[eq_idx + 1..].trim().replace(r"\:", ":").replace(r"\=", "=");
            map.insert(k, v);
        }
    }

    Ok(map)
}

/// Writes a key-value map to an Eclipse .prefs file with proper `\:` escaping.
pub fn write_prefs_file(path: &Path, props: &BTreeMap<String, String>) -> io::Result<()> {
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent)?;
    }

    let mut lines = Vec::new();
    for (k, v) in props {
        let escaped_v = v.replace(':', r"\:");
        lines.push(format!("{k}={escaped_v}\n"));
    }

    let mut file = File::create(path)?;
    for line in lines {
        file.write_all(line.as_bytes())?;
    }

    Ok(())
}

/// Synchronizes an environment entry into global `com.infor.erpln.jca.connectivity.cloudenv.prefs`.
pub fn sync_cloudenv_prefs(prefs_path: &Path, env_name: &str, config: &IonapiConfig) -> io::Result<()> {
    let mut props = read_prefs_file(prefs_path)?;
    let count: usize = props.get("EnvironmentsCount").and_then(|s| s.parse().ok()).unwrap_or(0);

    let mut target_idx = None;
    for i in 0..count {
        if props.get(&format!("EnvironmentName{i}")).map(|s| s.as_str()) == Some(env_name) {
            target_idx = Some(i);
            break;
        }
    }

    let idx = match target_idx {
        Some(i) => i,
        None => {
            props.insert("EnvironmentsCount".into(), (count + 1).to_string());
            count
        }
    };

    props.insert(format!("EnvironmentName{idx}"), env_name.to_string());
    props.insert(format!("TenantID{idx}"), config.tenant_id.clone());
    props.insert(format!("GatewayURL{idx}"), config.gateway_url.clone());
    props.insert(format!("AuthorizationCodeURL{idx}"), config.auth_url.clone());
    props.insert(format!("RequestTokenURL{idx}"), config.token_url.clone());
    props.insert(format!("RevokeTokenURL{idx}"), config.revoke_url.clone());
    props.insert(format!("ClientID{idx}"), config.client_id.clone());
    props.insert(format!("ClientSecret{idx}"), config.client_secret.clone());
    props.insert(format!("AppScope{idx}"), config.scope.clone());
    props.insert("eclipse.preferences.version".into(), "1".into());

    write_prefs_file(prefs_path, &props)
}

/// Reads workspace `com.infor.erpln.jca.connectivity.prefs` and groups properties by connection name.
pub fn read_connectivity_prefs(prefs_path: &Path) -> io::Result<HashMap<String, HashMap<String, String>>> {
    let props = read_prefs_file(prefs_path)?;
    let count: usize = props.get("ConfigurationCount").and_then(|s| s.parse().ok()).unwrap_or(0);
    let mut configs_by_name = HashMap::new();

    for i in 0..count {
        let name = match props.get(&format!("Name{i}")) {
            Some(n) if !n.is_empty() => n.clone(),
            _ => continue,
        };

        let mut cfg = HashMap::new();
        cfg.insert("_index".into(), i.to_string());

        let suffix = i.to_string();
        for (k, v) in &props {
            if k.ends_with(&suffix) {
                let attr_name = &k[..k.len() - suffix.len()];
                if !attr_name.is_empty() {
                    cfg.insert(attr_name.to_string(), v.clone());
                }
            }
        }

        configs_by_name.insert(name, cfg);
    }

    Ok(configs_by_name)
}

/// Synchronizes workspace `com.infor.erpln.jca.connectivity.prefs`.
pub fn sync_connectivity_prefs(
    prefs_path: &Path,
    env_name: &str,
    config: &IonapiConfig,
    project_name: Option<&str>,
) -> io::Result<()> {
    let mut props = read_prefs_file(prefs_path)?;
    let count: usize = props.get("ConfigurationCount").and_then(|s| s.parse().ok()).unwrap_or(8).max(8);
    props.insert("ConfigurationCount".into(), count.to_string());
    props.insert("eclipse.preferences.version".into(), "1".into());

    if !props.contains_key("Name0") {
        props.insert("Name0".into(), "Debug".into());
        props.insert("Description0".into(), "Debug Server".into());
        props.insert("State0".into(), "initial".into());
        props.insert("Company0".into(), "0".into());
        props.insert("Port0".into(), "0".into());
        props.insert("MaxConnections0".into(), "1".into());
        props.insert("MaxReferences0".into(), "-1".into());
        props.insert("IsStatic0".into(), "true".into());
    }

    // ProjectServer (Index 1)
    props.insert("Name1".into(), "ProjectServer".into());
    props.insert("Description1".into(), "Project Server".into());
    props.insert("ActivationType1".into(), "http_oauth2".into());
    props.insert("CloudEnvironment1".into(), env_name.to_string());
    props.insert("HostName1".into(), config.backend_webservice_url.clone());
    props.insert("Company1".into(), "0".into());
    props.insert("Port1".into(), "0".into());
    props.insert("MaxConnections1".into(), "1".into());
    props.insert("MaxReferences1".into(), "-1".into());
    props.insert("IsStatic1".into(), "true".into());
    props.insert("IsFixedCompany1".into(), "true".into());
    props.insert("State1".into(), "valid".into());
    props.insert("http_oauth21".into(), "true".into());
    props.insert("http_basic1".into(), "true".into());
    props.insert("bw1".into(), "true".into());
    props.insert("baanlogin1".into(), "true".into());

    let standard_conns = [
        ("RuntimeRepositoryConnection", "Runtime Repository"),
        ("TestServerConnection", "Test Server Connection"),
        ("TestBdeEventConnection", "Test BDE Event Connection"),
    ];

    for (offset, (name, desc)) in standard_conns.iter().enumerate() {
        let idx = offset + 2;
        props.insert(format!("Name{idx}"), name.to_string());
        props.insert(format!("Description{idx}"), desc.to_string());
        props.insert(format!("Company{idx}"), "0".into());
        props.insert(format!("Port{idx}"), "0".into());
        props.insert(format!("MaxConnections{idx}"), "1".into());
        props.insert(format!("MaxReferences{idx}"), "-1".into());
        props.insert(format!("IsStatic{idx}"), "true".into());
        props.insert(format!("SharedWith{idx}"), "ProjectServer".into());
        props.insert(format!("State{idx}"), "valid".into());
        props.insert(format!("ActivationType{idx}"), "bw".into());
        props.insert(format!("http_oauth2{idx}"), "true".into());
        props.insert(format!("http_basic{idx}"), "true".into());
        props.insert(format!("bw{idx}"), "true".into());
        props.insert(format!("baanlogin{idx}"), "true".into());
    }

    if let Some(proj) = project_name {
        let dev_name = format!("{proj}_dev");
        let rt_name = format!("{proj}_rt");

        props.insert("Name6".into(), dev_name.clone());
        props.insert("Description6".into(), format!("Development Address {dev_name}"));
        props.insert("ActivationType6".into(), "bw".into());
        props.insert("SharedWith6".into(), "ProjectServer".into());
        props.insert("Company6".into(), "0".into());
        props.insert("Port6".into(), "0".into());
        props.insert("MaxConnections6".into(), "1".into());
        props.insert("MaxReferences6".into(), "-1".into());
        props.insert("IsFixedCompany6".into(), "true".into());
        props.insert("State6".into(), "valid".into());
        props.insert("http_oauth26".into(), "true".into());
        props.insert("http_basic6".into(), "true".into());
        props.insert("bw6".into(), "true".into());

        props.insert("Name7".into(), rt_name.clone());
        props.insert("Description7".into(), format!("Runtime Address {rt_name}"));
        props.insert("ActivationType7".into(), "bw".into());
        props.insert("SharedWith7".into(), "ProjectServer".into());
        props.insert("Company7".into(), "0".into());
        props.insert("Port7".into(), "0".into());
        props.insert("MaxConnections7".into(), "1".into());
        props.insert("MaxReferences7".into(), "-1".into());
        props.insert("State7".into(), "valid".into());
        props.insert("http_oauth27".into(), "true".into());
        props.insert("http_basic7".into(), "true".into());
        props.insert("bw7".into(), "true".into());
    }

    write_prefs_file(prefs_path, &props)
}
