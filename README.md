# costgraph-superset
This includes the superset dashboard to visualise the costgraph information.


## Testing
Create a new values file that contains the configuration you'd like to deploy

```bash
helm template . -f <values-file> | tee | kubectl apply --dry-run=client -f -
```