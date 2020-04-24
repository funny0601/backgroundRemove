import argparse

def get_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--preview', default = 'no',
                        help='preview of attaching background image to the original video',
                        type=str, choices=['yes', 'no'])
    args = parser.parse_args()

    return args.preview