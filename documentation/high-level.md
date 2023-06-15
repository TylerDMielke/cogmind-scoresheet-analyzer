# High Level Design

``` mermaid
graph LR
    single_scoresheet[ScoreSheet.txt]
    scoresheet_loader(ScoreSheetLoader)
    ui(TextualUI)
    single_scoresheet --> scoresheet_loader --> ui

```