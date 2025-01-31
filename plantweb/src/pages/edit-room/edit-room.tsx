/* istanbul ignore file */
import React, { memo, useEffect } from "react";
import { Button, TextField, Stack, Grid } from "@mui/material";
import { useEditRoomLogic } from "./use-edit-room-logic";
import { useAppStyles } from "use-app-styles";
export type RoomByIDProps = {
  id: string;
};

export const EditRoomByID = memo(({ id }: RoomByIDProps) => {
  const { room, roomName, onGetRoomData, onRoomNameChange, onSubmit } =
    useEditRoomLogic(Number(id));

  useEffect(
    () => {
      onGetRoomData();
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    []
  );

  const { classes } = useAppStyles();

  return (
    <Grid
      container
      direction="row"
      justifyContent="center"
      alignItems="center"
      xs={12}
    >
      <Grid xs={12}>
        <h3 className={classes.page_title}>Edit {room?.name}</h3>
      </Grid>
      <Grid xs={12} style={{ marginBottom: 20 }}>
        <p>
          Complete the below fields to edit room details, avoid using existing
          room names.
        </p>
      </Grid>
      <Grid
        container
        direction="row"
        justifyContent="flex-end"
        alignItems="center"
        xs={12}
      >
        <Grid xs={12}>
          <TextField
            id="room-name"
            label="New Room Name"
            variant="outlined"
            value={roomName}
            onChange={onRoomNameChange}
          />
        </Grid>
      </Grid>
      <Grid
        container
        direction="row"
        justifyContent="flex-end"
        alignItems="center"
        xs={12}
      >
        <Grid xs={2}>
          <Stack spacing={2} direction="row">
            <Button variant="outlined" onClick={onSubmit}>
              Confirm
            </Button>
          </Stack>
        </Grid>
      </Grid>
    </Grid>
  );
});
