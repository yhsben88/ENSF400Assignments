"""
Writer: Hiu Sum Yuen
File_version: 1.1
"""
import ansible_runner

def cmd_run_playbook(playbook_dir):
    """
        Description: 
            Executes the playbook running command 'ansible-playbook /path/to/playbook.yml', 
            returning the result of running the command.
        Params:
            playbook_dir <str>: Relative path to playbook.
            result <tuple>: Represents 3 elements -> response message <str>
            , error message <str>, return code <int>.
    """
    command_to_execute = "ansible-playbook " + playbook_dir
    result = ansible_runner.interface.run_command(executable_cmd=command_to_execute)
    return result

def print_response(results):
    """
        Description: 
            Prints response message from results <tuple> of a runner function.
        Params:
            results <tuple>: Represents 3 elements -> response message <str>
            , error message <str>, return code <int>.
            response <str>: Response message of command execution.
            error_string <str>: Error message from command execution.
            return_code <int>: Return code for performance or state of command execution.
    """
    response, error_string, return_code = results
    print(f"Response: {response}")
    return

def main():
    playbook_path = "hello.yml"
    results = cmd_run_playbook(playbook_path)
    print_response(results)

if __name__ == "__main__":
    main()