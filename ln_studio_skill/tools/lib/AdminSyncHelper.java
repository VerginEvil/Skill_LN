package tools.lib;

import java.io.*;
import java.lang.reflect.Field;
import java.util.*;

public class AdminSyncHelper {

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
            e.printStackTrace();
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

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: java tools.lib.AdminSyncHelper <admin_file> <cmd> [args...]");
            System.exit(1);
        }

        File adminFile = new File(args[0]);
        String cmd = args[1];

        try {
            Class<?> compClass = Class.forName("com.infor.ln.studio.common.core.cm.administration.AdministrationComponent");
            HashMap<String, Object> map = loadAdmin(adminFile);

            if ("list".equalsIgnoreCase(cmd)) {
                System.out.println("TOTAL:" + map.size());
                for (Map.Entry<String, Object> entry : map.entrySet()) {
                    Object comp = entry.getValue();
                    System.out.println("ENTRY\t" + entry.getKey() + "\t" +
                        getField(comp, "isCreated") + "\t" +
                        getField(comp, "isCheckedout") + "\t" +
                        getField(comp, "m_isDirty") + "\t" +
                        getField(comp, "m_isVSCHappy")
                    );
                }
            } else if ("add".equalsIgnoreCase(cmd)) {
                if (args.length < 4) {
                    System.err.println("Usage: add <rel_path> <activity_folder>");
                    System.exit(1);
                }
                String relPath = args[2].replace('\\', '/');
                String actFolder = args[3];
                String fullPath = ":" + actFolder + "/" + relPath;

                Object comp = compClass.getDeclaredConstructor(String.class).newInstance(fullPath);
                setField(comp, "isCreated", true);
                setField(comp, "isCheckedout", false);
                setField(comp, "isEvercheckedIn", false);
                setField(comp, "m_isDirty", true);
                setField(comp, "m_isVSCHappy", false);
                setField(comp, "isExpired", false);

                map.put(relPath, comp);
                saveAdmin(adminFile, map);
                System.out.println("[OK] Added/Updated: " + relPath);
            } else if ("remove".equalsIgnoreCase(cmd)) {
                if (args.length < 3) {
                    System.err.println("Usage: remove <rel_path>");
                    System.exit(1);
                }
                String relPath = args[2].replace('\\', '/');
                if (map.remove(relPath) != null) {
                    saveAdmin(adminFile, map);
                    System.out.println("[OK] Removed: " + relPath);
                } else {
                    System.out.println("[WARN] Not found: " + relPath);
                }
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
