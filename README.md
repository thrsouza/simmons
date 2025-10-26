# 🎯 Simmons

[![Python](https://img.shields.io/badge/Python->=3.10,<3.14-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-1.2.0+-orange.svg)](https://github.com/joaomdmoura/crewai)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A technical documentation generation tool that transforms video transcripts into clear, structured documentation using AI.**

Simmons leverages the power of AI agents to convert verbal knowledge from video transcriptions into professional, well-formatted technical documentation. Perfect for creating documentation from recorded meetings, tutorials, technical presentations, and educational content.

## ✨ Features

- 🤖 **AI-Powered Processing**: Uses multiple specialized AI agents for content creation, review, and formatting
- 🧠 **Advanced Reasoning**: Enhanced AI reasoning capabilities for optimal content generation and formatting
- 📝 **Multi-Language Support**: Generate documentation in multiple languages
- 🔄 **Sequential Workflow**: Technical writer → Content reviewer → Markdown specialist
- 📋 **Structured Output**: Creates well-formatted Markdown documentation with proper sections
- 🎯 **Topic-Focused**: Tailors content generation to specific technical topics
- 📊 **Comprehensive Coverage**: Automatically captures all topics mentioned in transcriptions, including implicit ones
- 🚀 **Command Line Interface**: Easy-to-use CLI for quick processing

## 🏗️ Architecture

Simmons uses the CrewAI framework to orchestrate three specialized AI agents with enhanced reasoning capabilities:

1. **Technical Content Writer**: Interprets and restructures transcription content into clear, technical language with advanced reasoning
2. **Content Reviewer**: Reviews and refines the content for clarity and technical accuracy
3. **Markdown Specialist**: Converts the reviewed content into well-formatted Markdown documentation with reasoning-based optimization

### 🧠 AI Agent Features

- **Enhanced Reasoning**: Technical Content Writer and Markdown Specialist agents use advanced reasoning with up to 3 attempts for optimal results
- **Comprehensive Coverage**: Automatically includes all topics mentioned in transcriptions, even implicit ones
- **Quality Assurance**: Multi-layer review process ensures technical accuracy and clarity

## 🚀 Quick Start

### Prerequisites

- Python 3.10 to 3.13
- An OpenAI API key (for GPT-4o-mini model)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/thrsouza/simmons.git
   cd simmons
   ```

2. **Install dependencies**:
   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -e .
   ```

3. **Set up your OpenAI API key**:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

### Basic Usage

```bash
# Generate documentation from a transcript file
python -m simmons.main -t "Python Programming" -f transcript.txt -l "en-US"

# Or using the installed package
simmons -t "Docker Containers" -f meeting_transcript.txt -l "pt-BR"
```

### Parameters

- `-t, --topic`: Topic for the documentation generation (e.g., "Python Programming", "Docker Containers")
- `-f, --file`: Path to the transcription file (required)
- `-l, --language`: Language for the documentation (default: "en-US")

## 📖 Usage Examples

### Example 1: Technical Tutorial Documentation

```bash
python -m simmons.main \
  --topic "REST API Development" \
  --file tutorial_transcript.txt \
  --language "en-US"
```

This will generate a file named `REST API Development.md` with structured documentation.

### Example 2: Meeting Notes in Portuguese

```bash
python -m simmons.main \
  --topic "Arquitetura de Microsserviços" \
  --file reuniao_transcript.txt \
  --language "pt-BR"
```

### Example 3: Workshop Documentation

```bash
python -m simmons.main \
  --topic "Machine Learning Fundamentals" \
  --file workshop_transcript.txt \
  --language "en-US"
```

## 📄 Input Format

Simmons accepts plain text transcription files. The transcription should contain:

- Spoken content from videos, meetings, or presentations
- Natural language explanations of technical concepts
- Any verbal knowledge you want to convert to documentation

**Example transcript file**:
```
So today we're going to talk about Docker containers. Docker is a containerization platform that allows you to package applications with their dependencies. Let me explain how this works...
```

## 📊 Output Format

Simmons generates Markdown documentation with the following structure:

```markdown
# 🎯 [Topic Name]

**📋 TL;DR**
- Summary point 1
- Summary point 2
- Summary point 3

## 📝 [Section Title]
Content with proper formatting...

## 🔧 [Another Section]
More structured content...
```

## 🛠️ Configuration

The AI agents are configured through YAML files in `simmons/config/`:

- `agents.yaml`: Defines the roles, goals, and backstories of the AI agents
- `tasks.yaml`: Defines the tasks each agent performs, their expected outputs, and processing rules

### Recent Improvements

- **Enhanced Topic Coverage**: The system now automatically includes all topics mentioned in transcriptions, even if not explicitly stated as section titles
- **Improved Model Configuration**: Updated to use explicit OpenAI model specification (`openai/gpt-4o-mini`) for better reliability
- **Advanced Reasoning**: Technical Content Writer and Markdown Specialist agents now use reasoning capabilities with multiple attempts for optimal results

You can customize these configurations to adjust the behavior and output style of the generated documentation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Thiago Souza**
- Email: dev@thiagosouza.com
- GitHub: [@thrsouza](https://github.com/thrsouza)

## 🙏 Acknowledgments

- [CrewAI](https://github.com/crewAIInc/crewAI) - For the amazing AI agent framework
- [OpenAI](https://openai.com) - For providing the GPT-4o-mini model

---

**Made with ❤️ for the developer community**
