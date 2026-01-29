from strands import Agent, tool
from strands.models.bedrock import BedrockModel
from strands_tools import calculator, use_aws, current_time

# Test the agent
@tool
def test_agent() -> str:
    """Run test cases for the agent to verify calculator, web search, AWS, and time functionality."""
    results = []
    
    try:
        print("🧪 Testing Calculator...")
        response = agent("What is 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100?")
        results.append("\n✅ Calculator test passed")
    except Exception as e:
        results.append(f"\n❌ Calculator test failed: {str(e).split(':')[-1].strip()}")
        
    
    try:
        print("🧪 Testing Current Time (UTC and ICT)...")
        response = agent("What time is it now in UTC and ICT timezone?")
        results.append("\n✅ Current time test passed")
    except Exception as e:
        results.append(f"\n❌ Current time test failed: {str(e).split(':')[-1].strip()}")
    
    try:
        print("🧪 Testing List 10 x S3 Bucket...")
        response = agent("List ten S3 Buckets")
        results.append("\n✅ Use AWS to list 10 S3 buckets test passed")
    except Exception as e:
        results.append(f"\n❌ Use AWS to list 10 S3 buckets test failed: {str(e).split(':')[-1].strip()}")
    
    
    return "\n".join(results)

# TODO: Edit System Prompt and Model's id using your custom model deployment arn.
# System prompt and agent initialization
system_prompt = """You are a helpful AI assistant with access to calculator, web search, AWS services, and time tools. 
You provide clear, accurate responses and use tools when needed to help users with their queries.
Always explain your reasoning and be friendly in your interactions. Please use the same languages as the users to provide chain of though and response"""

model_id = "arn:aws:bedrock:us-east-1:<your account id>:custom-model-deployment/<deploymentid>"

tools = [calculator, use_aws, current_time] 

agent = Agent(
    model=BedrockModel(
        model_id=model_id,
        region_name = "us-east-1"
    ),
    tools=tools,
    system_prompt=system_prompt,
    name="CustomNovaAgent"
)

def main():
    import boto3
    
    print("\n" + "=" * 60)
    print("💬 Strands Agent Chat Interface")
    print("=" * 60)
    model_name = model_id
    try:
        bedrock = boto3.client('bedrock', region_name='us-east-1')        
        importedID = bedrock.get_custom_model_deployment(customModelDeploymentIdentifier=model_id)
        model_name = importedID['modelArn'].split(':',5)[5].split('/',1)[1]
        print(f"\n🤖 Custom Model: {model_name}")
    except Exception as e:
        model_name = model_id
        print(f"\n🤖 Model: {model_id}")

    print("\n🛠️  Available Tools:")
    print("   🧮 calculator     - Perform mathematical operations")
    print("   ☁️  use_aws        - Interact with AWS services")
    print("   🕐 current_time   - Get current time in any timezone")
    print("\n📝 Commands:")
    print("   💬 Type your questions naturally")
    print("   🧪 Type 'test' to run agent tests")
    print("   👋 Type 'exit' or 'quit' to end conversation")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 Goodbye!")
                break
            
            if user_input.lower() == 'test':
                print("\n🤖 Agent: Running tests...\n")
                print(test_agent())
                continue
            
            
            print("\n🤖 Agent:", end=" ")
            response = agent(user_input)
            print()  # New line after streaming completes
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e).split(':')[-1].strip()}")

# Chat interface
if __name__ == "__main__":
    main();