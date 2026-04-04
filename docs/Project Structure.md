# Project Structure

The repository follows a standard Python package layout where all source code is inside `algonest/` and project-level assets stay at repository root.

```text
project_root/
|
+-- algonest/
|   +-- __init__.py
|   +-- arrays/
|   +-- dynamic_programming/
|   +-- graphs/
|   +-- heap/
|   +-- linked_list/
|   +-- math/
|   +-- search/
|   +-- sort/
|   +-- stack_queue/
|   +-- strings/
|   +-- trees/
|   +-- utils/
|
+-- tests/
+-- docs/
+-- benchmarks/
+-- pyproject.toml
+-- README.md
```

Notes:

- All algorithm implementations live under `algonest/`.
- Test modules live under top-level `tests/`.
- Benchmark scripts live under top-level `benchmarks/`.
- Documentation files live under top-level `docs/`.
