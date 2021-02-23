.. _prerequisites:

Prerequisites - What you need to run Fenix Library - Running
**************************************************************

**Note**: Currently, the **Fenix Library** only supports **Arch Linux** and its derivatives (like *RebornOS*, *EndeavourOS*, *Manjaro*, etc.).

**Warning**: Please skip this section if you have already run the setup script successfully.

1. **Install python dev tools**: 

    * Install the packages :code:`python` and :code:`pip`. In Arch Linux, for example, you would run 

    .. code-block:: bash
        
        sudo pacman -S --needed python python-pip

3. **Install other packages**: (*Only required if installing from Git*) Install :code:`git`, :code:`base-devel`, and :code:`linux-headers`. In Arch Linux, for example, you would run 

    .. code-block:: bash
            
        sudo pacman -S --needed git base-devel linux-headers