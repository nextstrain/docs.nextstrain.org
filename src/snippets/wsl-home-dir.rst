.. admonition:: For WSL on Windows installs
   :class: hint

   By default, your Windows home directory will not be directly accessible under your WSL home directory. When run in a WSL prompt, the following command fixes that by creating a symlink to it in your WSL home directory. This allows you to use Windows-based text editors and Linux commands all on the same files.

   .. code-block:: bash

         ln -ws "$(wslpath "$(wslvar USERPROFILE)")" ~/windows_home

   Optionally, you can customize the ``windows_home`` folder name or only link to a specific directory under your windows user (e.g. ``ln -ws "$(wslpath "$(wslvar USERPROFILE)")/Documents" ~/windows_documents``).

   If the command does not work, you may have to first run ``sudo apt install wslu``.
