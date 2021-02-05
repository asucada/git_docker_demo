c = get_config() #get the config object
c.IPKernelApp.pylab = 'inline' #in-line figure when using Matplotlib
c.Notebook.ip = '*'
c.Notebook.allow_remote_access = True
c.NotebookApp.open_browser = False #do not open a browserwindow by default when using notebooks
c.NotebookApp.token = '' #No token. Always use jupyter over ssh tunnel
c.NotebookApp.notebook_dir = '/notebooks'
c.NotebookApp.allow_root = True #allow to run jupyter from root user inside Docker container
