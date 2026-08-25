@@
- yield ModbusWorkModeSelectDescription(  
-     key="work_mode",  
-     address=[  
-         ModbusAddressSpec(holding=49203, models=Inv.EVO_10_H),  
-     ],  
-     name="Work Mode",  
-     options_map={          # read map — what the inverter returns  
-         1: "Self Use",  
-         2: "Feed-in First",  
-         3: "Back-up",  
-         4: "Peak Shaving",  
-     },  
-     write_options_map={    # write map — what the inverter accepts  
-         0: "Self Use",  
-         1: "Feed-in First",  
-         2: "Back-up",  
-         3: "Peak Shaving",  
-     },  
- )
+    yield ModbusWorkModeSelectDescription(  
+        key="work_mode",  
+        address=[  
+            ModbusAddressSpec(holding=49203, models=Inv.EVO_10_H),  
+        ],  
+        name="Work Mode",  
+        # Read map — what the inverter returns. We include 0 as an alias for "Self Use"
+        # because the inverter briefly reflects the written value (0) from its write-cache
+        # before the next poll confirms the read-back as 1; adding 0 -> "Self Use" prevents
+        # a transient "Unknown" being shown in HA. The UI dedupes identical labels.
+        options_map={
+            0: "Self Use",  # write-cache alias (brief window after write)
+            1: "Self Use",  # confirmed read-back value
+            2: "Feed-in First",
+            3: "Back-up",
+            4: "Peak Shaving",
+        },
+        # Write map — numeric values to write (what the inverter accepts). EVO10 expects 0-based writes.
+        write_options_map={
+            0: "Self Use",
+            1: "Feed-in First",
+            2: "Back-up",
+            3: "Peak Shaving",
+        },
+    )
*** End Patch
