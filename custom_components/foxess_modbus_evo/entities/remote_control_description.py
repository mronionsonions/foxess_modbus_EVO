@@
-                work_mode_map={
-                    WorkMode.SELF_USE: 1,
-                    WorkMode.FEED_IN_FIRST: 2,
-                    WorkMode.BACK_UP: 3,
-                },
+                # EVO10 uses 0-based values for writes to 49203 (but returns 1-based values on read).
+                # Use 0-based write values here so the remote-control fallback write is correct.
+                work_mode_map={
+                    WorkMode.SELF_USE: 0,
+                    WorkMode.FEED_IN_FIRST: 1,
+                    WorkMode.BACK_UP: 2,
+                },
*** End Patch
