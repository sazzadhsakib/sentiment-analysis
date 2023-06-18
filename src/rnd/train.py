from datasets import load_dataset
from sentence_transformers.losses import CosineSimilarityLoss

from setfit import SetFitModel, SetFitTrainer, sample_dataset

# load custom datasets
dataset = load_dataset('csv', data_files={
    'train': ['train.csv'],
    'eval': ['eval.csv']},
    cache_dir="./data/"
)

# Load a SetFit model from Hub
model = SetFitModel.from_pretrained(
    "StatsGary/setfit-ft-sentinent-eval",
    
)
# Create trainer
trainer = SetFitTrainer(
    model=model,
    train_dataset=dataset['train'],
    eval_dataset=dataset['eval'],
    loss_class=CosineSimilarityLoss,
    metric="accuracy",
    batch_size=16,
    num_iterations=20,  # The number of text pairs to generate for contrastive learning
    num_epochs=1,  # The number of epochs to use for contrastive learning
    column_mapping={"text": "text", "label": "label"}  # Map dataset columns to text/label expected by trainer
)

# Train and evaluate
trainer.train()
metrics = trainer.evaluate()

# save
trainer.model._save_pretrained(save_directory="./output/")