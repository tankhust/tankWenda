package com.tank.async;

import java.util.List;

/**
 * Created by tank on 2018/7/30.
 */
public interface EventHandler {
    void doHandle(EventModel model);

    List<EventType> getSupportEventTypes();
}
