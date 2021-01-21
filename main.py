from nagios_plugin import Plugin


if __name__ == '__main__':
    plugin = Plugin()
    print("Hello world.")
    plugin.return_ok(message="printed hello world", perf_data="abc=123;")
