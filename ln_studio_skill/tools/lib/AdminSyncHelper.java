package tools.lib;

import java.io.*;
import java.lang.reflect.Field;
import java.util.*;

/**
 * AdminSyncHelper
 * Byte-accurate serializer and state machine for Eclipse Infor LN Studio .admin files.
 *
 * Enforces:
 * 1. Exact project-relative paths without leading slash or :<activityFolder>/ prefix
 *    in both HashMap key and AdministrationComponent.m_path.
 * 2. CMStudio authentic state machine transitions:
 *    - after_get
 *    - after_create
 *    - after_checkout
 *    - after_put
 *    - after_checkin
 *    - after_uncheckout
 * 3. Exclusion and repair of standalone script files (.src, .4gl, .dal, .clnsrc, .rptdsrc).
 */
public class AdminSyncHelper {

    private static final Set<String> EXCLUDED_EXTENSIONS = new HashSet<>(Arrays.asList(
        ".src", ".4gl", ".dal", ".clnsrc", ".rptdsrc"
    ));

    public static String normalizeRelPath(String path) {
        if (path == null) {
            return "";
        }
        String p = path.replace('\\', '/').trim();
        while (p.startsWith("/")) {
            p = p.substring(1);
        }
        if (p.startsWith(":")) {
            int slash = p.indexOf('/');
            if (slash != -1) {
                p = p.substring(slash + 1);
            } else {
                p = p.substring(1);
            }
        }
        while (p.startsWith("/")) {
            p = p.substring(1);
        }
        return p;
    }

    private static Object getField(Object obj, String fieldName) {
        try {
            Field f = obj.getClass().getDeclaredField(fieldName);
            f.setAccessible(true);
            return f.get(obj);
        } catch (Exception e) {
            return null;
        }
    }

    private static void setField(Object obj, String fieldName, Object val) {
        try {
            Field f = obj.getClass().getDeclaredField(fieldName);
            f.setAccessible(true);
            f.set(obj, val);
        } catch (Exception e) {
            // ignore field set failures
        }
    }

    @SuppressWarnings("unchecked")
    public static HashMap<String, Object> loadAdmin(File adminFile) throws Exception {
        if (!adminFile.exists()) {
            return new HashMap<>();
        }
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(adminFile))) {
            return (HashMap<String, Object>) ois.readObject();
        }
    }

    public static void saveAdmin(File adminFile, HashMap<String, Object> map) throws Exception {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(adminFile))) {
            oos.writeObject(map);
        }
    }

    private static Object createComponent(Class<?> compClass, String normPath) throws Exception {
        Object comp = compClass.getDeclaredConstructor(String.class).newInstance(normPath);
        setField(comp, "m_path", normPath);
        return comp;
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: java tools.lib.AdminSyncHelper <admin_file> <cmd> [args...]");
            System.exit(1);
        }

        File adminFile = new File(args[0]);
        String cmd = args[1].toLowerCase(Locale.ROOT);

        try {
            Class<?> compClass = Class.forName("com.infor.ln.studio.common.core.cm.administration.AdministrationComponent");
            HashMap<String, Object> map = loadAdmin(adminFile);

            if ("list".equals(cmd)) {
                System.out.println("TOTAL:" + map.size());
                for (Map.Entry<String, Object> entry : map.entrySet()) {
                    Object comp = entry.getValue();
                    System.out.println("ENTRY\t" + entry.getKey() + "\t" +
                        getField(comp, "isCreated") + "\t" +
                        getField(comp, "isCheckedout") + "\t" +
                        getField(comp, "isEvercheckedIn") + "\t" +
                        getField(comp, "isExpired") + "\t" +
                        getField(comp, "m_isDirty") + "\t" +
                        getField(comp, "m_isVSCHappy") + "\t" +
                        getField(comp, "m_path")
                    );
                }
            } else if ("add".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: add <rel_path> [activity_folder]");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = createComponent(compClass, normPath);
                setField(comp, "isCreated", true);
                setField(comp, "isCheckedout", true);
                setField(comp, "isEvercheckedIn", false);
                setField(comp, "m_isDirty", true);
                setField(comp, "m_isVSCHappy", false);
                setField(comp, "isExpired", false);

                map.put(normPath, comp);
                saveAdmin(adminFile, map);
                System.out.println("[OK] Added/Updated: " + normPath);
            } else if ("remove".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: remove <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object removed = map.remove(normPath);
                if (removed == null) {
                    removed = map.remove(args[2].replace('\\', '/'));
                }
                if (removed != null) {
                    saveAdmin(adminFile, map);
                    System.out.println("[OK] Removed: " + normPath);
                } else {
                    System.out.println("[WARN] Not found: " + normPath);
                }
            } else if ("init".equals(cmd)) {
                saveAdmin(adminFile, map);
                System.out.println("[OK] Initialized empty .admin: " + adminFile.getAbsolutePath());
            } else if ("after_get".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: after_get <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = map.get(normPath);
                if (comp == null) {
                    comp = createComponent(compClass, normPath);
                    map.put(normPath, comp);
                }
                setField(comp, "m_path", normPath);
                setField(comp, "isCreated", false);
                setField(comp, "isCheckedout", false);
                setField(comp, "isEvercheckedIn", false);
                setField(comp, "isExpired", false);
                setField(comp, "m_isDirty", false);
                setField(comp, "m_isVSCHappy", true);
                saveAdmin(adminFile, map);
                System.out.println("[OK] after_get: " + normPath);
            } else if ("after_create".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: after_create <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = map.get(normPath);
                if (comp == null) {
                    comp = createComponent(compClass, normPath);
                    map.put(normPath, comp);
                }
                setField(comp, "m_path", normPath);
                setField(comp, "isCreated", true);
                setField(comp, "isCheckedout", true);
                setField(comp, "isEvercheckedIn", false);
                setField(comp, "isExpired", false);
                setField(comp, "m_isDirty", true);
                setField(comp, "m_isVSCHappy", false);
                saveAdmin(adminFile, map);
                System.out.println("[OK] after_create: " + normPath);
            } else if ("after_checkout".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: after_checkout <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = map.get(normPath);
                if (comp == null) {
                    comp = createComponent(compClass, normPath);
                    map.put(normPath, comp);
                }
                setField(comp, "m_path", normPath);
                setField(comp, "isCreated", false);
                setField(comp, "isCheckedout", true);
                setField(comp, "isEvercheckedIn", false);
                setField(comp, "isExpired", false);
                setField(comp, "m_isDirty", false);
                setField(comp, "m_isVSCHappy", true);
                saveAdmin(adminFile, map);
                System.out.println("[OK] after_checkout: " + normPath);
            } else if ("after_put".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: after_put <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = map.get(normPath);
                if (comp == null) {
                    comp = createComponent(compClass, normPath);
                    map.put(normPath, comp);
                }
                setField(comp, "m_path", normPath);
                setField(comp, "isCheckedout", true);
                setField(comp, "m_isDirty", false);
                saveAdmin(adminFile, map);
                System.out.println("[OK] after_put: " + normPath);
            } else if ("after_checkin".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: after_checkin <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = map.get(normPath);
                if (comp == null) {
                    comp = createComponent(compClass, normPath);
                    map.put(normPath, comp);
                }
                setField(comp, "m_path", normPath);
                setField(comp, "isCreated", false);
                setField(comp, "isCheckedout", false);
                setField(comp, "isEvercheckedIn", true);
                setField(comp, "isExpired", false);
                setField(comp, "m_isDirty", false);
                setField(comp, "m_isVSCHappy", true);
                saveAdmin(adminFile, map);
                System.out.println("[OK] after_checkin: " + normPath);
            } else if ("after_uncheckout".equals(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: after_uncheckout <rel_path>");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                Object comp = map.get(normPath);
                if (comp != null) {
                    Boolean isCreated = (Boolean) getField(comp, "isCreated");
                    Boolean isEver = (Boolean) getField(comp, "isEvercheckedIn");
                    if (Boolean.TRUE.equals(isCreated) && !Boolean.TRUE.equals(isEver)) {
                        map.remove(normPath);
                        saveAdmin(adminFile, map);
                        System.out.println("[OK] after_uncheckout (removed uncommitted): " + normPath);
                        System.exit(0);
                    }
                    setField(comp, "m_path", normPath);
                    setField(comp, "isCreated", false);
                    setField(comp, "isCheckedout", false);
                    setField(comp, "isEvercheckedIn", false);
                    setField(comp, "isExpired", false);
                    setField(comp, "m_isDirty", false);
                    saveAdmin(adminFile, map);
                    System.out.println("[OK] after_uncheckout (reverted): " + normPath);
                } else {
                    System.out.println("[WARN] after_uncheckout: not found " + normPath);
                }
            } else if ("repair".equals(cmd)) {
                HashMap<String, Object> cleanMap = new HashMap<>();
                int cleanedCount = 0;
                for (Map.Entry<String, Object> entry : map.entrySet()) {
                    String rawKey = entry.getKey();
                    String normPath = normalizeRelPath(rawKey);
                    // Check exclusion
                    String lower = normPath.toLowerCase(Locale.ROOT);
                    boolean excluded = false;
                    for (String ext : EXCLUDED_EXTENSIONS) {
                        if (lower.endsWith(ext)) {
                            excluded = true;
                            break;
                        }
                    }
                    if (excluded) {
                        cleanedCount++;
                        continue;
                    }
                    Object comp = entry.getValue();
                    setField(comp, "m_path", normPath);
                    cleanMap.put(normPath, comp);
                }
                saveAdmin(adminFile, cleanMap);
                System.out.println("[OK] Repaired .admin, cleaned " + cleanedCount + " entries. Total: " + cleanMap.size());
            } else if ("set-status".equals(cmd)) {
                if (args.length < 6) {
                    System.err.println("Usage: set-status <rel_path> <isCreated> <isCheckedOut> <isDirty> [isVSCHappy]");
                    System.exit(1);
                }
                String normPath = normalizeRelPath(args[2]);
                boolean isCreated = Boolean.parseBoolean(args[3]);
                boolean isCheckedOut = Boolean.parseBoolean(args[4]);
                boolean isDirty = Boolean.parseBoolean(args[5]);
                boolean isVSCHappy = args.length > 6 ? Boolean.parseBoolean(args[6]) : false;

                Object comp = map.get(normPath);
                if (comp == null) {
                    comp = createComponent(compClass, normPath);
                    map.put(normPath, comp);
                }
                setField(comp, "m_path", normPath);
                setField(comp, "isCreated", isCreated);
                setField(comp, "isCheckedout", isCheckedOut);
                setField(comp, "m_isDirty", isDirty);
                setField(comp, "m_isVSCHappy", isVSCHappy);
                setField(comp, "isExpired", false);
                saveAdmin(adminFile, map);
                System.out.println("[OK] Updated status: " + normPath);
            } else {
                System.err.println("Unknown command: " + cmd);
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(2);
        }
    }
}
