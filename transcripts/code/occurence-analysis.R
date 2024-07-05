library(glmmTMB)
library(stats)
library(broom)
library(conflicted)  
library(tidyverse)
conflict_prefer("filter", "dplyr")
conflict_prefer("lag", "dplyr")
library(data.table)
library(mltools)
library(ggplot2)

# Load Data
df <- read.csv('large_data.csv', header=TRUE, stringsAsFactors=FALSE)
df <- df[, !names(df) %in% c("X")]
head(df, 3)

unique(df['Child_Age'])

# df <- df %>% filter(Salient!=0)

model <- glm(
    data = df,
    formula = Occurs ~
        Salient
        *
        Child_Age
    ,
    family = binomial)

summary(model)

# df <- df %>% filter(Salient!=0)
# df %>% group_by(Child_Age) %>% summarize(prob_o = sum(Occurs)/(sum(Salient)))
