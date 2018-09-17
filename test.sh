#!/bin/bash
ln -sf "$PWD/test.sh" .git/hooks/pre-commit

(cd app; pylint app);
rc=$?;
if [[ $rc != 0 ]];
then
    echo "Fix pylint"
    exit $rc;
fi

docker-compose exec -T web python app/manage.py test;
rc=$?;
if [[ $rc != 0 ]];
then
    echo "Fix unittests"
    exit $rc;
fi

echo "Tests pass";
exit 0;
