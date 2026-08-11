The `archived/` folder contains the ALD/E experimental and simulation data needed to reproduce the experiments presented in our ESWC 2025 paper that introduced this software:

> Sadruddin, S. et al. (2025). *LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models.* In: Curry, E., et al. *The Semantic Web. ESWC 2025.* Lecture Notes in Computer Science, vol. 15719. Springer, Cham. https://doi.org/10.1007/978-3-031-94578-6_14

The remaining contents are organized as follows for running the tutorial notebook:

```text
data/
├── stage1/
│   ├── process.txt
│   ├── process-description.pdf
│   ├── feedback/
│   └── schema/
│
├── stage2/
│   ├── batch1/
│   ├── batch2/
│   ├── feedback-batch1/
│   ├── feedback-batch2/
│   ├── schema-batch1/
│   └── schema-batch2/
│
└── stage3/
    ├── batch1/
    ├── batch2/
    ├── feedback-batch1/
    ├── schema-batch1/
    └── schema-batch2/
```

The specific process selected is `Metal Organic Cages Synthesis`. This is one of the founding processes of https://scischema.org/ . Note that for stage2 we have deliberately reduced the papers per batch from 5 to just 2 for faster processing times. Same for stage3 we have deliberately reduced the papers from 25 per batch to 3 per batch for faster notebook processing. Ideally this is best run as a job launched directly on the GPU server.