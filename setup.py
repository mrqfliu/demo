from setuptools import setup
setup(
    name="demo",
    version="0.1.0",
    install_requires=[],  # 主依赖（根据实际情况填写）
    extras_require={
        "docs": [
            "recommonmark",
            "sphinx_markdown_tables",
            "sphinx_rtd_theme>=2.0.0",
        ]
    },  # 注意此处是闭合的 } 和逗号
)
