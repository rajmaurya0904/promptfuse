# Promptfuse

**A Claude Code skill that automatically evaluates prompt templates against test datasets for regressions, token efficiency, and safety boundaries right inside the terminal.**

<!-- THE PROBLEM: 2-3 concrete lines on the annoying thing this removes. -->

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

<!-- 3-6 bullets: what it checks, computes or produces. -->

## Limitations

**Limitations**

- Relies on external language model APIs (e.g., Anthropic Claude); if the service is unavailable or the model version changes, evaluations may fail.
- Subject to provider rate limits; large test suites can hit request quotas and cause throttling.
- Evaluation is deterministic only when the underlying model is deterministic; nondeterministic model responses can lead to flaky regression checks.
- Does not currently support offline or open‑source model back‑ends.


## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
