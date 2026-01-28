# Strands Agent with Nova Pro

This example demonstrates a Strands Agent using Amazon Nova Pro with calculator, AWS services, and time tools.

## Setup

### Using pip
```bash
pip install -r requirements.txt
```

### Using uv
```bash
uv sync
```

## Usage

### Interactive Chat Mode

Using pip:
```bash
python agent.py
```

Using uv:
```bash
uv run agent.py
```

Commands:
- Type your questions naturally
- Type `test` to run agent tests
- Type `exit` or `quit` to end the conversation

### Example Interactions
```
👤 You: What time is it now in UTC and ICT timezone?
🤖 Agent: [Returns current time in both timezones]

👤 You: List ten S3 Buckets
🤖 Agent: [Lists 10 S3 buckets from your AWS account]

👤 You: What is 25 multiplied by 4?
🤖 Agent: The product of 25 and 4 is 100.

👤 You: test
🤖 Agent: Running tests...
✅ Calculator test passed
✅ Current time test passed
✅ Use AWS to list 10 S3 buckets test passed
```

## Tools

- **calculator**: Performs mathematical operations
- **use_aws**: Interact with AWS services (list buckets, describe instances, etc.)
- **current_time**: Get current date and time in any timezone

## Model Configuration

Currently using: `us.amazon.nova-pro-v1:0` (inference profile)

### Optional: Using Fine-Tuned Model

After fine-tuning completes:

1. Create deployment:
```bash
aws bedrock create-custom-model-deployment \
  --custom-model-arn <your-custom-model-arn> \
  --deployment-name nova-pro-custom-deployment \
  --region us-east-1
```

2. Update `model_id` in agent.py with deployment ARN

## Example Queries

- "What is 25 multiplied by 4?"
- "What time is it in Tokyo?"
- "List my S3 buckets"
- "Describe my EC2 instances"
