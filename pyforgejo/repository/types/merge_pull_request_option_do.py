# This file was auto-generated by Fern from our API Definition.

import typing

MergePullRequestOptionDo = typing.Union[
    typing.Literal[
        "merge",
        "rebase",
        "rebase-merge",
        "squash",
        "fast-forward-only",
        "manually-merged",
    ],
    typing.Any,
]
