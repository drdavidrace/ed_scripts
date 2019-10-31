# Status Management For Educational Scripts

The educational scripts in Colaboratory present a unique set of requirements:

1. They will generally be run in the sandbox; therefore, logging information to the disk is not really an option.
2. They need to have a simple way of turning on verbose.
3. They should be able to print log information to the screen so students can _screen capture_ the output.

With these requirements in mind, this python class is designed to collect the execution environment status and display the associated status.