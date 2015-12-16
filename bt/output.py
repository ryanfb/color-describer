import sys

from bt import config


def output_results(results, split_id='results', output_stream=None):
    '''
    Log `results` readably to `output_stream`, with a header
    containing `split_id`, and dump the results in JSON format
    to "`split_id`.json" in the run directory.

    :param results: a dictionary of summary statistics from an evaluation
    :type results: dict(str -> object)

    :param str split_id: an identifier for the source of `results` (e.g. 'dev')

    :param file output_stream: the file-like object to which to log the results
        (default: stdout)
    :type split_id: str
    '''
    if output_stream is None:
        output_stream = sys.stdout

    output_stream.write('----- %s -----\n' % split_id)
    for name in sorted(results.keys()):
        output_stream.write('%s.%s: %s\n' % (split_id, name, repr(results[name])))

    output_stream.flush()

    config.dump_pretty(results, '%s.results.json' % split_id)
