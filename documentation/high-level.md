# High Level Design

## Graphs/Diagrams
``` mermaid
graph LR
    single_scoresheet[ScoreSheet.txt]
    scoresheet_loader(ScoreSheetLoader)
    ui(TextualUI)
    single_scoresheet --> scoresheet_loader --> ui

```