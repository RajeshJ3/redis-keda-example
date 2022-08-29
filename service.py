def run(*args, **kwargs):
    '''
    run is entry point for the service
    '''
    print("[START] Service Begin")

    # TODO: replace the following cide with actual service code
    # currently sleeping for 10s, to demonstrate a long running process.
    from time import sleep
    sleep(10)

    print("[DONE] Service Completed")
