CLAAT Preview Link: https://codelabs-preview.appspot.com/?file_id=16_qjTsxV4dfyPo2Ni60gBfFIXtjn0Sk-IKDV99dqyTg#0

CLAAT Document Link: https://docs.google.com/document/d/16_qjTsxV4dfyPo2Ni60gBfFIXtjn0Sk-IKDV99dqyTg/edit


## Part2
### Attribution Modeling
Attribution modeling is a framework for analyzing which touchpoints, or marketing channels, receive credit for a conversion. Each attribution model distributes the value of a conversion across each touchpoint differently. A model comparison tool allows you to analyze how each model distributes the value of a conversion. There are six common attribution models: First Interaction, Last Interaction, Last Non-Direct Click, Linear, Time-Decay, and Position-Based.

![image](https://user-images.githubusercontent.com/33648410/106234377-ba2f1a00-61c6-11eb-8060-dba70fe2e64b.png)

By analyzing each attribution model, one can get a better idea of the ROI for each marketing channel/campaign.

Types of Marketing Models we will be implementing-

### Single-Touch Attribution Models
Single-touch attribution models assign 100% of conversion credit to one marketing touchpoint. Even if a customer saw 20 ads before converting, single-touch attribution will determine that only 1 of the 20 ads deserves conversion credit.
Single-touch attribution models are easy to implement because of their low level of complexity. They’re also the most popular attribution models because of their historical tie to Google Ads
The models are
1. First Touch Attribution (FTA)
2. Last Touch Attribution (LTA)

### Multi-Touch Attribution Models:
Multi-touch attribution is best described in contrast to its counterpart, single-touch attribution.
In order to divide the revenue credit for a sale properly, multi-touch attribution uses weighted modeling in order to allocate credit to the plethora of influential channels, campaigns, keywords, and touchpoints.
Weighted touchpoint modeling assigns a percentage of the revenue credit for a customer to an array of touchpoints, as defined by the respective multi-touch attribution model chosen by the organization.
The models are:
1. Logistic Regression Model
2. Time-decay Attribution Model
3. Linear Attribution Model
4. U-Shaped Attribution Model



## Data

We have to use the Criteo Attribution Bidding Dataset and build Attribution models to optimize the Budget Allocation for various Marketing campaigns.

This dataset represents a sample of 30 days of Criteo live traffic data. Each line corresponds to one impression (a banner) that was displayed to a user. For each banner we have detailed information about the context, if it was clicked, if it led to a conversion and if it led to a conversion that was attributed to Criteo or not.
