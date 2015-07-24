# Riava Switch Docs

### Set controller

```
$ vi /usr/local/etc/lagopus/lagopus.conf
```
Edit `controller {A.B.C.D;}` to your controller IP.

### Start lagopus
```
./start_lagopus.sh
```

### Stop lagopus

```
./stop_lagopus.sh
```

### Enter into CLI

```
$ lagosh
```

or in `lagopus` folder

```
$ lagopus/src/config/cli/lagosh
```

### Display table information
```
show table
```

### Display flow information
```
show flow
```

### Show controller information
```
show controller A.B.C.D
```
