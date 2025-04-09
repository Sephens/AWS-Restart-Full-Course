# Creating a Git Repository - Comprehensive Lab Guide

## Lab Overview
This lab walks through the process of setting up a GitHub repository to manage your Python projects. You'll learn to:
- Download existing project files
- Create a GitHub account
- Understand GitHub basics
- Set up a private repository
- Upload and download project files

## Exercise 1: Downloading Python Files

### Steps to Download Project Files
1. In your IDE:
   - Navigate to **File > Download Project**
   - This creates a compressed (ZIP) file on your local machine
2. Locate the downloaded file (typically in your Downloads folder)
3. Extract the contents:
   - **Windows**: Right-click → "Extract All"
   - **Mac**: Double-click the ZIP file

**Best Practices:**
- Create a dedicated folder for your AWS Restart projects
- Maintain clear naming conventions (e.g., `lab1-loops`, `lab2-conditionals`)
- Verify all files are present after extraction

## Exercise 2: Creating a GitHub Account

### Account Setup Process
1. Visit [github.com](https://www.github.com)
2. Click "Sign up"
3. Enter required information:
   - Username (professional recommendations)
   - Email address
   - Secure password
4. Verify your email address

**Pro Tips:**
- Use an email you'll have long-term access to
- Consider enabling two-factor authentication
- Upload a profile picture for professional recognition

## Exercise 3: GitHub Hello World Guide

### Key Concepts from the Guide
1. **Repositories**: Project folders containing all files
2. **Branches**: Parallel versions of your code
3. **Commits**: Saved changes with descriptive messages
4. **Pull Requests**: Proposing and reviewing changes
5. **Merging**: Combining changes into main branch

**Navigation:**
- The guide is available at:
  [GitHub Hello World](https://guides.github.com/activities/hello-world/)

## Exercise 4: Creating a Private Repository

### Repository Creation Steps
1. Click the "+" icon → "New repository"
2. Configure repository:
   - Name: `aws_restart` (or similar)
   - Description: "AWS Restart program labs and projects"
   - Visibility: **Private**
   - Initialize with README: **Checked**
3. Click "Create repository"

### Uploading Files
1. In your new repository, click "Upload files"
2. Drag-and-drop or select all extracted files from Exercise 1
3. Add commit message (e.g., "Initial lab upload")
4. Click "Commit changes"

**Important Notes:**
- Private repositories ensure your work isn't publicly visible
- README.md serves as your project documentation
- Clear commit messages help track changes

## Exercise 5: Downloading Repository

### Download Options
1. **Clone (Recommended for Ongoing Work):**
   ```bash
   git clone https://github.com/your-username/aws_restart.git
   ```
   Requires Git installed locally

2. **Download ZIP (Simple One-Time Download):**
   - Click "Code" → "Download ZIP"
   - Save to your `aws_restart` folder
   - Extract contents

### Verification
After extraction:
1. Check file structure matches original
2. Verify all Python files open correctly
3. Ensure no corruption during transfer

## Going Beyond the Lab

### Regular GitHub Workflow
1. **Daily Work Pattern:**
   ```bash
   git pull origin main      # Get latest changes
   # Make your code edits
   git add .                # Stage changes
   git commit -m "Message"  # Describe changes
   git push origin main     # Upload changes
   ```

2. **Branching Strategy:**
   ```bash
   git checkout -b new-feature  # Create branch
   # Make changes
   git push origin new-feature
   # Then create Pull Request on GitHub
   ```

### .gitignore Setup
Create a `.gitignore` file to exclude:
- Python cache (`__pycache__/`)
- Environment files (`.env`)
- IDE settings (`.vscode/`)

Example content:
```
# Python
__pycache__/
*.py[cod]

# Environment
.env
.venv
venv/

# IDE
.vscode/
.idea/
```

## Troubleshooting Common Issues

1. **Authentication Problems:**
   - Use SSH keys or GitHub CLI for smoother access
   - Consider PAT (Personal Access Token) if password fails

2. **Large File Uploads:**
   - GitHub has 100MB file size limit
   - For larger files, use Git LFS (Large File Storage)

3. **Sync Conflicts:**
   - Always `git pull` before starting work
   - Use `git status` frequently to check state

## Security Best Practices

1. **Repository Visibility:**
   - Keep student work private
   - Make public only when required

2. **Sensitive Data:**
   - Never commit:
     - API keys
     - Passwords
     - Configuration secrets
   - Use environment variables instead

3. **Access Control:**
   - Carefully manage collaborator access
   - Review all incoming pull requests

## Integrating with Python Workflow

### Version Control Benefits
1. **Experiment Safely:**
   ```bash
   git checkout -b experiment
   # Try new code risk-free
   ```

2. **Track Changes:**
   ```bash
   git log --oneline  # View condensed history
   git diff HEAD~1    # Compare with previous
   ```

3. **Collaborate Efficiently:**
   - Use Issues for task tracking
   - Leverage Projects for kanban-style management

## Visual GitHub Clients

For those preferring GUIs:
1. **GitHub Desktop**: Official client (user-friendly)
2. **GitKraken**: Powerful cross-platform client
3. **VS Code Git Integration**: Built-in to popular IDE

## Advanced Topics to Explore

1. **GitHub Actions**: Automate testing/deployment
2. **Pages**: Host project documentation
3. **Codespaces**: Cloud-based development environments
4. **Projects**: Agile project management

## Final Checklist

1. [ ] All lab files downloaded and extracted
2. [ ] GitHub account created and verified
3. [ ] Hello World guide reviewed
4. [ ] Private repository created
5. [ ] Files successfully uploaded
6. [ ] Repository downloaded and verified
7. [ ] Regular commit practice established

By completing this lab, you've established a professional version control workflow that will support all your future programming projects. Remember to commit frequently with meaningful messages to maintain a clear project history.