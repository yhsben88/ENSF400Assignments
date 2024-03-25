"""
Writer: Hiu Sum Yuen
File_version: 1.2
"""
import ansible_runner
import subprocess

def cmd_run_playbook(playbook_dir):
    """
        Description: 
            Executes the playbook running command 'ansible-playbook /path/to/playbook.yml', 
            returning the result of running the command.
        Params:
            playbook_dir <str>: Relative path to playbook.
        Variables:
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
        variables:
            response <str>: Response message of command execution.
            error_string <str>: Error message from command execution.
            return_code <int>: Return code for performance or state of command execution.
    """
    response, error_string, return_code = results
    print(f"Response: {response}")
    return

def run_curl():
    """
        Description:
            Runs the curl http://0.0.0.0 command.
        Variables:
            curl_output <str>: Information relevent to the curl command.
    """
    curl_output = subprocess.run(["curl" , "http://0.0.0.0"], text=True)
    print() # print new line.
    return curl_output

def main():
    playbook_path = "hello.yml"
    cmd_run_playbook(playbook_path)
    for i in range(3):
        run_curl()

if __name__ == "__main__":
    main()