import { ChangeEvent, useCallback, useState } from "react";
import { useHistory } from "react-router-dom";

import { useRooms } from "shared/hooks/use-rooms";
import { PATHS } from "shared/constants";

export const useAddRoomLogic = () => {
  const [roomName, setRoomName] = useState("");

  const { postRoom } = useRooms();

  const history = useHistory();

  const onRoomNameChange = useCallback(
    ({ target: { value } }: ChangeEvent<HTMLInputElement>) => {
      setRoomName(value);
    },
    [setRoomName]
  );

  const onSubmit = useCallback(async () => {
    const newRoom = await postRoom(roomName);
    if (newRoom) {
      history.push(`${PATHS.rooms}/${newRoom.id}`);
    }
  }, [postRoom, history, roomName]);

  return {
    roomName,
    onRoomNameChange,
    onSubmit,
  };
};
