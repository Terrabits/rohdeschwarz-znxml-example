# rohdeschwarz znxml example

This is a minimal example project which uses the rohdeschwarz Vna driver to:

-   open SCPI log
-   connect to instrument
-   log instrument info
-   basic instrument setup
-   save local `.znxml` file
-   preset instrument
-   recall previously saved, local `.znxml` file
-   check for (log) errors
-   clear errors (if present)
-   close log (implied; on `__delete__()`)
-   close instrument connection (implied; on `__delete__()`)

## Requirements

Note that `ZNA` and `.znxml` support requires `rohdeschwarz~=1.5.0`. See `requirements.txt`.

The example was validated with Python `3.8.5` `x64` on macOS Catalina `10.15.7`; the exact python package versions (i.e. `pip freeze`) are included in `requirements-lock.txt`.
