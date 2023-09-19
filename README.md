## An In-Depth Measurement Analysis of 5G mmWave PHY Latency and its Impact on End-to-End Delay

In this repository, we release the dataset and tools in PAM '23 paper, [*An In-Depth Measurement Analysis of 5G mmWave PHY Latency and its Impact on End-to-End Delay*] 

This is a measurement paper with several types of experiments conducted for different purposes having different methodologies. To help you quickly navigate and have the ability to understand the different pieces, we have created different folders for different experiments. There are README files within each folder that provide instructions on validating the experiment-specific artifacts. At the very top of the README instructions, we also specify which results/plots (e.g. Figure 2 in the paper) the folder is responsible. Lastly, to make it easy here are some generic principles we followed for releasing the artifacts:

#### Dataset Sizes
- If the dataset is small enough, we included the dataset file in this repository itself. 
- If the dataset files are huge, we use a small sample of the dataset in the repository to demonstrate the functionality/correctness.

#### Artifacts and Info

- If data analysis is involved, our instructions will contain information on how to process the data. 
- No matter what the dataset size is, we provide the fully generated results and/or plots. If you decide to run the analysis and/or plotting scripts, the outcome of processing will create the raw results files in the repository.


## Generating plots
We have built scripts that uses the dataset provided to generate the plots shown in our paper. More specifically, the scripts will print the Figure it generates. 

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.3.4)
- Matplotlib (>= 3.5.1)
- Seaborn (>= 0.11.2)

### Running code

After cloning the repository, navigate to `Artifacts` folder and simply run the specific command for the section plots you wish to generate. An example is given below:

`python plot-section4.1.py`

If everything succeeded, a `final_plots` folder should be created with all the figures in `.pdf` format.

As always, if there are any questions, feel free to reach out to us (<fezeu001@umn.edu>)! 
