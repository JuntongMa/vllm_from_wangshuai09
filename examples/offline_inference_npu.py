from vllm import LLM, SamplingParams

# Sample prompts.
prompts = [
    # "Hello, my name is",
    # "The president of the United States is",
    "美国的首都是"
    # "The capital of France is",
    # "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(max_tokens=100, temperature=0.8, top_p=0.95)

# Create an LLM.
# llm = LLM(model="facebook/opt-125m")
llm = LLM(model="Qwen/Qwen2-7B-Instruct")
# Generate texts from the prompts. The output is a list of RequestOutput objects
# that contain the prompt, generated text, and other information.
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")