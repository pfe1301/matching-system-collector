import argparse
import json
import logging
# from api import get_data
from utils import preprocess_entity, build_strategy
from tqdm.auto import tqdm

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "file", help="File that contains entities to get description for")
    parser.add_argument(
        "-o",
        "--output",
        default="../store/output.json",
        help="Location of the output"
    )
    parser.add_argument(
        "-l",
        "--lang",
        default="en",
        help="Specify the language"
    )

    parser.add_argument(
        "-t",
        "--type",
        default="job",
        help="Enitities types"
    )

    parser.add_argument(
        "-s",
        "--strategy",
        default="writesonic",
        help="The strategy of data collection (data source)",
    )

    args = parser.parse_args()

    # Configure the logger
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.INFO)

    logger.info(f"Collecting data using {args.strategy} strategy")
    strategy = build_strategy(args.strategy)

    logger.info(f"Loading {args.type} entities")
    with open(args.file, "r") as entities_file:
        entities = entities_file.readlines()

    logger.info("Loading entities descriptions")
    if args.type == 'job':
        jobs_desc = []
        with open(args.output, 'a') as output_fp:
            for entity in tqdm(entities):
                entity = preprocess_entity(entity)
                data = strategy.get_data(
                    entity=entity,
                    type=args.type,
                    lang=args.lang
                )
                jobs_desc.append({
                    'entity': entity,
                    'description': data
                })

            logger.info("Saving entities descriptions")

            json.dump(jobs_desc, output_fp)
    else:
        # skills
        skills_desc = []
        with open(args.output, "a") as output_fp:
            for entity in tqdm(entities):
                entity = preprocess_entity(entity)
                data = strategy.get_data(
                    entity=entity,
                    type=args.type,
                    lang=args.lang
                )
                skills_desc.append({
                    "entity": entity,
                    'description': data
                })
            logger.info("Saving entities descriptions")
            json.dump(skills_desc, output_fp)
