# models

This folder is for `r2c` models. They broadly follow the allennlp configuration format. If you want r2c, you'll want to look at `multiatt`.

## Replicating validation results
Here's how you can replicate my val results. Run the command(s) below. First, you might want to make your GPUs available. When I ran these experiments I used

`source activate r2c2 && export LD_LIBRARY_PATH=/usr/local/cuda-10.1/ && export PYTHONPATH=/home/woosik/PycharmProjects/VCR && export CUDA_VISIBLE_DEVICES=0`

- For question answering, run:
```
python models/train.py -params models/multiatt/default.json -folder models/saves/flagship_answer 
```

- for Answer justification, run
```
python models/train.py -params models/multiatt/default.json -folder models/saves/flagship_rationale -rationale
```

You can combine the validation predictions using
`python models/eval_q2ar.py -answer_preds models/saves/flagship_answer/valpreds.npy -rationale_preds models/saves/flagship_rationale/valpreds.npy`

## Submitting to the leadrboard(from VCR origininal github)

VCR features a [leaderboard](https://visualcommonsense.com/leaderboard/) where you can submit your answers on the test set. Submitting to the leaderboard is easy! You'll need to submit something like [the example submission CSV file](https://s3-us-west-2.amazonaws.com/ai2-rowanz/r2c/example-submission.csv). You can use the `eval_for_leaderboard.py` script, which formats everything in the right way.

Essentially, your submission has to have the following columns:

```
annot_id,answer_0,answer_1,answer_2,answer_3,rationale_conditioned_on_a0_0,rationale_conditioned_on_a0_1,rationale_conditioned_on_a0_2,rationale_conditioned_on_a0_3,rationale_conditioned_on_a1_0,rationale_conditioned_on_a1_1,rationale_conditioned_on_a1_2,rationale_conditioned_on_a1_3,rationale_conditioned_on_a2_0,rationale_conditioned_on_a2_1,rationale_conditioned_on_a2_2,rationale_conditioned_on_a2_3,rationale_conditioned_on_a3_0,rationale_conditioned_on_a3_1,rationale_conditioned_on_a3_2,rationale_conditioned_on_a3_3
```

To evaluate, I'll first take the argmax over the answer choices, then take the argmax over your rationale choices (conditioned on the right answers).
These give two sets of predictions, which can be used to compute Q->A and QA->R accuracy. For Q->AR accuracy, we take a bitwise AND between the hits of the QA and QAR columns. In other words, to get a question right, you have to get the answer AND the rationale right.
