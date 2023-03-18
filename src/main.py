import argparse
import json
import logging
# from api import get_data
from utils import preprocess_entity, build_strategy
from tqdm.auto import tqdm
import os

logger = logging.getLogger(__name__)

api_key = os.getenv("OPENAI_API_KEY")


def save_data(data, output, start_index):
    file_name = output + start_index + '_' + str(start_index + len(data)) + '.json'
    with open(file_name, "w") as output_file:
        json.dump(data, output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "file", help="File that contains entities to get description for")
    parser.add_argument(
        "-o",
        "--output",
        default="../store/output",
        help="Location of the output (default: ../store/output) (without extension))"
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

    parser.add_argument(
        "-c",
        "--chunk",
        default=100,
        help="The number of entities to store in a single file",
    )

    # start index
    parser.add_argument(
        "-si",
        "--startindex",
        default=0,
        help="The index of the entity to start from",
    )

    # end index
    parser.add_argument(
        "-ei",
        "--endindex",
        default=-1,
        help="The index of the entity to end at",
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

    descriptions = []
    count = 0
    number_chunk = 0
    if args.endindex == -1:
        args.endindex = len(entities)
    for entity in tqdm(entities[int(args.startindex):int(args.endindex)]):
        try:
            entity = preprocess_entity(entity)
            data = strategy.get_data(
                entity=entity,
                type=args.type,
                lang=args.lang
            )
            descriptions.append({
                "entity": entity,
                'description': data
            })
            count += 1
            logger.info(f"Got description for {entity}")
            if count % args.chunk == 0:
                save_data(descriptions, args.output, args.start_index + number_chunk * args.chunk + 1)
                descriptions = []
                number_chunk += 1
                
        except Exception as e:
            logger.error(e)
            logger.info("Stopped at entity: " + entity + " with index: " + str(count))
            save_data(descriptions, args.output, args.start_index + number_chunk * args.chunk + 1)
            descriptions = []
            raise e

    if len(descriptions) > 0:
        save_data(descriptions, args.output, args.start_index + number_chunk * args.chunk + 1)
