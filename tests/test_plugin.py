import pytest

from nagios_plugin import Plugin
from nagios_plugin.plugin import get_plugin_output


def test_plugin_return_ok_return_code():
    with pytest.raises(SystemExit) as excinfo:
        plugin = Plugin()
        plugin.return_ok()

    assert excinfo.value.code == 0


def test_plugin_return_warning_return_code():
    with pytest.raises(SystemExit) as excinfo:
        plugin = Plugin()
        plugin.return_warning()

    assert excinfo.value.code == 1


def test_plugin_return_critical_return_code():
    with pytest.raises(SystemExit) as excinfo:
        plugin = Plugin()
        plugin.return_critical()

    assert excinfo.value.code == 2


def test_plugin_return_unknown_return_code():
    with pytest.raises(SystemExit) as excinfo:
        plugin = Plugin()
        plugin.return_unknown()

    assert excinfo.value.code == 3


example_message_and_perf_data = [
        (None, None, ""),
        ("test 123", None, "test 123"),
        ("test 123", "/=2643MB;5986;0;5986;", "test 123 | /=2643MB;5986;0;5986;"),
    ]


@pytest.mark.parametrize(
    "message, perf_data, expected",
    example_message_and_perf_data
)
def test_plugin_std_out_of_str(capsys, message, perf_data, expected):
    with pytest.raises(SystemExit) as _:
        plugin = Plugin()
        plugin.return_ok(message=message, perf_data=perf_data)
    captured = capsys.readouterr()
    assert captured.out.rstrip() == expected


@pytest.mark.parametrize(
    "message, perf_data, expected",
    example_message_and_perf_data
)
def test_get_plugin_output(message, perf_data, expected):
    output_data = get_plugin_output(message, perf_data)
    assert output_data == expected
