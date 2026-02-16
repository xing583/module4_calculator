from app.calculator import Calculator


def run_inputs(inputs):
    it = iter(inputs)
    outputs = []

    def fake_input(_=""):
        return next(it)

    def fake_output(msg):
        outputs.append(msg)

    Calculator().run(input_func=fake_input, output_func=fake_output)
    return outputs


def test_help():
    out = run_inputs(["help", "exit"])
    assert any("Commands:" in x for x in out)


def test_history_empty():
    out = run_inputs(["history", "exit"])
    assert "No history yet." in out


def test_empty_input():
    out = run_inputs(["", "exit"])
    assert "Please enter a command." in out


def test_invalid_format():
    out = run_inputs(["add 1", "exit"])
    assert any("Invalid format" in x for x in out)


def test_invalid_numbers():
    out = run_inputs(["add a b", "exit"])
    assert any("Invalid numbers" in x for x in out)


def test_divide_by_zero():
    out = run_inputs(["divide 1 0", "exit"])
    assert any("Error:" in x for x in out)


def test_unknown_operation():
    out = run_inputs(["power 2 3", "exit"])
    assert any("Error:" in x for x in out)


def test_success_and_history():
    out = run_inputs(["add 2 3", "history", "exit"])
    assert "5.0" in out
    assert any("=" in x for x in out)


def test_exit():
    out = run_inputs(["exit"])
    assert "Goodbye!" in out

def test_unexpected_error_branch(monkeypatch):
    from app import calculator as calc_module

    def boom(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(calc_module.CalculationFactory, "create", boom)

    it = iter(["add 1 2", "exit"])
    outputs = []

    def fake_input(_=""):
        return next(it)

    def fake_output(msg):
        outputs.append(msg)

    Calculator().run(input_func=fake_input, output_func=fake_output)

    assert any("Unexpected error:" in x for x in outputs)
