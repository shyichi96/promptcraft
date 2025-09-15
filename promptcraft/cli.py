import typer
import openai
import os
from dotenv import load_dotenv
from promptcraft.core import load_prompt, fill_prompt

app = typer.Typer()
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.command()
def prompt(
    prompt: str = typer.Option(..., help="Tên prompt (VD: summarization)"),
    input: str = typer.Option(..., help="Dữ liệu đầu vào cho prompt"),
):
    template = load_prompt(prompt)
    content = fill_prompt(template, {"input": input})

    typer.echo("⏳ Đang gửi prompt đến OpenAI...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
    )
    typer.echo("\n🧠 Phản hồi từ AI:\n")
    typer.echo(response["choices"][0]["message"]["content"])
