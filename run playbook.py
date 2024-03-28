from ansible_runner import Runner

def run_playbook():
    # Create Runner object
    r = Runner(
        playbook='hello.yml',
        inventory='inventory.ini'
    )

    # Run playbook
    r.run()

    # Print playbook results
    for event in r.events:
        if event['event'] == 'playbook_on_task_start':
            print("Task: {}".format(event['task']))

        if event['event'] == 'runner_on_failed':
            print("Task failed: {}".format(event['event_data']['task']))

if __name__ == "__main__":
    run_playbook()