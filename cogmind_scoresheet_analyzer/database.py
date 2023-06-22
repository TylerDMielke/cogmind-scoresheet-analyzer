import sqlite3 as sql
from pathlib import Path

# from cogmind_scoresheet_analyzer.logging_config import get_logger
#
# logger = get_logger(__name__)


class CogmindScoresheetAnalyzerDB:
    conn: sql.Connection

    def __init__(self):
        data_dir: Path = Path("data")
        if not data_dir.exists():
            try:
                data_dir.mkdir(exist_ok=True)
            except Exception as ex:
                # logger.exception("Failed to create data directory.")
                raise ex

        self.conn = sql.connect("data/csa.db")
        self._create_scoresheet_table()

    def _create_scoresheet_table(self):
        """Create the scoresheet table."""

        table_def: str = """
        CREATE TABLE IF NOT EXISTS scoresheet (
            id integer PRIMARY KEY,
            run_date text NOT NULL,
            player text NOT NULL,
            result text NOT NULL
        );
        """

        cursor: sql.Cursor = self.conn.cursor()
        cursor.execute(table_def)
        cursor.close()


if __name__ == "__main__":
    db = CogmindScoresheetAnalyzerDB()
    # logger.info("Successfully instantiated the Cogmind Scoresheet Analyzer database.")
