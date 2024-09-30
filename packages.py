import subprocess
import sys

# =======================================
# List of dependencies to install
#
# Add your depencies here
# =======================================
dependencies = [
    "prettytable"
]


def install_package(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_pip():
    """Check if pip is installed, and install if it's not."""
    try:
        import pip
        print("pip is already installed.")
    except ImportError:
        print("pip is not installed. Installing pip...")
        # Ensure pip is installed
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
    
    print("\033c", end="")

def InitializePackages():
    # Check if pip is installed
    check_and_install_pip()

    dependencies_list = dependencies

    for package in dependencies_list:
        try:
            install_package(package)
            print(f"Installed {package}.")
        except Exception as e:
            print(f"Failed to install {package}: {e}")
    
    print("\033c", end="")

if __name__ == "__main__":
    InitializePackages()
