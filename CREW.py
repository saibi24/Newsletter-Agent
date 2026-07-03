from crewai import Crew, Process
import streamlit as st
from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

st.title("🤖 AI Research Crew")

topic = st.text_input(
    "Enter a topic",
    "Artificial Intelligence in Finance"
)

if st.button("Generate Report"):
    crew = Crew(
    agents = [researcher,writer,proof_reader],
    tasks=[research_task,write_task,proof_read_task],
    process=Process.sequential,
    verbose= True
)
    with st.spinner("Crew is working..."):
        result = crew.kickoff(inputs={"topic": topic})

    st.success("Done!")

    st.markdown(str(result))


